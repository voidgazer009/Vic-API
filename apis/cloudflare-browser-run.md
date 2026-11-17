# Cloudflare Browser Run

> AI抓取｜云端浏览器与网页转 Markdown

- 方向：一人公司｜分类：AI抓取
- 收录：第 011 期（2026-11-17），额度核对日期见当期
- 网址：https://developers.cloudflare.com/browser-rendering/platform/pricing/

**网址**：https://developers.cloudflare.com/browser-rendering/platform/pricing/ ；文档 https://developers.cloudflare.com/browser-run/

**注册**：注册 Cloudflare 账号，在控制台创建 API 令牌

**额度**：Workers 免费版每天 10 分钟浏览器时间，最多 3 个并发浏览器；付费版每月含 10 小时，超出每小时 $0.09

**用法**：调用 /markdown、/screenshot、/pdf、/scrape、/json 等 Quick Actions 接口，认证用 Authorization: Bearer YOUR_API_KEY

**Agent 适配**：官方提供 MCP 服务器，并支持 Puppeteer、Playwright、Stagehand

**场景**：让 Agent 抓取需要渲染的商家官网，转 Markdown 后做背调

**匹配度**：★★★★★


[返回目录](../README.md)