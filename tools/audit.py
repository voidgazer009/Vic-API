#!/usr/bin/env python3
"""Vic-API 发布前安全审核（REVIEW.md 的机器关卡）。
用法: python3 tools/audit.py [--live] [--issue NNN]
退出码 0 = 全部通过才允许推送。只用标准库。
"""
import csv, json, os, re, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = "--live" in sys.argv
ISSUE = sys.argv[sys.argv.index("--issue") + 1] if "--issue" in sys.argv else None
DIRS = ["外贸", "物流", "自媒体", "一人公司"]
REQUIRED = ["网址", "注册", "额度", "用法", "Agent 适配", "场景", "匹配度"]
TEXT_EXT = {".md", ".json", ".csv", ".py", ".txt", ".yml", ".yaml", ""}
ALLOWED_EXT = TEXT_EXT | {".pdf", ".png", ".jpg", ".webp"}
MAX_BYTES = 15 * 1024 * 1024

# S1 密钥与凭证特征
SECRET_PATTERNS = {
    "OpenAI/Anthropic key": r"sk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}",
    "GitHub token": r"gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}",
    "Google API key": r"AIza[0-9A-Za-z_-]{35}",
    "AWS key": r"AKIA[0-9A-Z]{16}",
    "Slack token": r"xox[abprs]-[A-Za-z0-9-]{10,}",
    "Stripe key": r"(?:sk|rk)_live_[A-Za-z0-9]{20,}",
    "Private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "Bearer token": r"Bearer\s+[A-Za-z0-9._-]{30,}",
    "JWT": r"eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",
    "key=value secret": r"(?i)(?:api[_-]?key|secret|password|passwd|token)\s*[=:]\s*['\"][A-Za-z0-9_\-]{16,}['\"]",
}
# S2 个人信息
PII_PATTERNS = {
    "邮箱": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "手机号(中国)": r"(?<!\d)1[3-9]\d{9}(?!\d)",
    "身份证号": r"(?<!\d)\d{17}[\dXx](?!\d)",
    "银行卡号": r"(?<!\d)(?:\d[ -]?){15,18}\d(?!\d)",
}
PII_ALLOW = re.compile(r"noreply|users\.noreply\.github\.com|example\.(com|org)|@(?:v\d|latest|types)", re.I)

problems, warnings = [], []
def bad(rule, msg): problems.append(f"[{rule}] {msg}")
def warn(rule, msg): warnings.append(f"[{rule}] {msg}")


def tracked_files():
    try:
        out = subprocess.run(["git", "-C", ROOT, "ls-files", "-co", "--exclude-standard"], capture_output=True, text=True, check=True).stdout
        return [f for f in out.splitlines() if f]
    except Exception:
        return [os.path.relpath(os.path.join(d, f), ROOT) for d, _, fs in os.walk(ROOT) if ".git" not in d for f in fs]


def check_files():
    for rel in tracked_files():
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p): continue
        ext = os.path.splitext(rel)[1].lower()
        name = os.path.basename(rel)
        if name.startswith(".env") or ext in {".pem", ".key", ".p12", ".pfx"} or name in {"id_rsa", "credentials.json", "token.json"}:
            bad("S3", f"禁止提交的敏感文件: {rel}")
        if ext not in ALLOWED_EXT: bad("S3", f"不允许的文件类型: {rel}")
        if os.path.getsize(p) > MAX_BYTES: bad("S3", f"文件过大(>15MB): {rel}")
        if "__pycache__" in rel or ext == ".pyc": bad("S3", f"缓存文件: {rel}")
        if ext not in TEXT_EXT or rel == "tools/audit.py": continue
        txt = open(p, encoding="utf-8", errors="ignore").read()
        for k, pat in SECRET_PATTERNS.items():
            for m in re.finditer(pat, txt):
                bad("S1", f"{rel}: 疑似 {k}: {m.group(0)[:12]}…")
        for k, pat in PII_PATTERNS.items():
            for m in re.finditer(pat, txt):
                s = m.group(0)
                if PII_ALLOW.search(s): continue
                if k == "银行卡号" and not luhn(re.sub(r"\D", "", s)): continue
                bad("S2", f"{rel}: 疑似{k}: {s[:6]}…")


def luhn(n):
    d = [int(c) for c in n][::-1]
    return sum(x if i % 2 == 0 else (x * 2 - 9 if x * 2 > 9 else x * 2) for i, x in enumerate(d)) % 10 == 0


def check_data():
    path = os.path.join(ROOT, "apis.json")
    if not os.path.exists(path): return bad("Q1", "缺少 apis.json")
    apis = json.load(open(path, encoding="utf-8"))
    names = [a["name"].lower() for a in apis]
    for n in set(x for x in names if names.count(x) > 1): bad("Q2", f"重复收录: {n}")
    for a in apis:
        tag = f"{a['issue']}/{a['name']}"
        if a.get("direction") not in DIRS: bad("Q1", f"{tag}: 方向无效 {a.get('direction')}")
        url = a.get("url", "")
        if not url.startswith("https://"): bad("Q3", f"{tag}: 网址必须是 https: {url!r}")
        miss = [k for k in REQUIRED if not a["fields"].get(k)]
        if miss: bad("Q1", f"{tag}: 缺字段 {miss}")
        q = a["fields"].get("额度", "")
        if q and not re.search(r"\d|以.{0,30}为准|无限制|不限", q): bad("Q4", f"{tag}: 额度既无数字也未写「以官方控制台为准」类说明")
        if re.search(r"(?i)\b(guaranteed|unlimited forever)\b|永久无限|保证免费", q): warn("Q4", f"{tag}: 额度措辞绝对化，请复核")
        if not os.path.exists(os.path.join(ROOT, "apis", f"{a['slug']}.md")): bad("Q1", f"{tag}: 缺卡片 apis/{a['slug']}.md")
    issues = sorted({a["issue"] for a in apis})
    latest = ISSUE or (issues[-1] if issues else None)
    cur = [a for a in apis if a["issue"] == latest]
    if latest and len(cur) != 10: bad("Q5", f"第 {latest} 期应为 10 条，实际 {len(cur)}")
    if latest and int(latest) >= 10:
        miss = [d for d in DIRS if not any(a["direction"] == d for a in cur)]
        if miss: bad("Q5", f"第 {latest} 期缺少方向: {miss}")
    # 核对日期：最新一期 md 必须声明
    md = [f for f in os.listdir(os.path.join(ROOT, "issues")) if f.startswith(f"issue-{latest}-")]
    if md:
        head = open(os.path.join(ROOT, "issues", md[0]), encoding="utf-8").read(600)
        if int(latest) >= 9 and not re.search(r"额度均于 \d{4}-\d{2}-\d{2} 核对", head): bad("Q4", f"第 {latest} 期缺少「额度均于 YYYY-MM-DD 核对官方页面」")
    if not any(f.startswith(f"Vic-API精选-第{latest}期") for f in os.listdir(os.path.join(ROOT, "pdf"))): bad("Q6", f"第 {latest} 期缺 PDF")
    if LIVE:
        for a in cur:
            try:
                req = urllib.request.Request(a["url"], method="GET", headers={"User-Agent": "Mozilla/5.0 Vic-API-audit"})
                code = urllib.request.urlopen(req, timeout=15).status
                if code >= 400: bad("Q3", f"{a['name']}: 网址返回 {code}")
            except urllib.error.HTTPError as e:
                (warn if e.code in (401, 403, 405, 429) else bad)("Q3", f"{a['name']}: 网址 HTTP {e.code}")
            except Exception as e:
                warn("Q3", f"{a['name']}: 网址无法访问 ({type(e).__name__})")
    return apis


def check_readme(apis):
    r = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    for a in apis or []:
        if f"apis/{a['slug']}.md" not in r: bad("Q7", f"README 未收录 {a['name']}")
    for link in re.findall(r"\]\(((?!https?://)[^)#]+)\)", r):
        if not os.path.exists(os.path.join(ROOT, link)): bad("Q7", f"README 失效相对链接: {link}")


if __name__ == "__main__":
    check_files()
    apis = check_data()
    check_readme(apis)
    for w in warnings: print("WARN ", w)
    for p in problems: print("FAIL ", p)
    print(f"\n审核结果: {len(problems)} problems, {len(warnings)} warnings")
    sys.exit(1 if problems else 0)
