# REST Countries

> 外贸数据｜国家币种区号速查

- 方向：外贸｜分类：外贸数据
- 收录：第 003 期（2026-11-09），额度核对日期见当期
- 网址：https://restcountries.com

**网址**：https://restcountries.com ；定价 https://restcountries.com/pricing

**注册**：restcountries.com 点 Get an API key → 邮箱注册（免费，无需信用卡）→ 建 Key

**额度**：Free $0，每月 1,000 次请求、2 个 API Key、数据每 24 小时同步；页面注明所有计划支持商用，并含全部接口和字段

**用法**：GET https://api.restcountries.com/countries/v5/codes.alpha_2/CA ，请求头 Authorization: Bearer {KEY} ；可用 ?response_fields= 只取需要的字段

**Agent 适配**：JSON 结构化、字段可裁剪，省 token；覆盖 250+ 国家、90+ 字段（币种、语言、国家区号、时区、边界等）

**场景**：Agent 写开发信时自动匹配客户国家的语言、币种和时区；报价单自动带当地货币

**匹配度**：★★★★☆


[返回目录](../README.md)