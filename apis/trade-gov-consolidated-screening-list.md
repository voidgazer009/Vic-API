# Trade.gov Consolidated Screening List

> 外贸合规｜出口受限名单

- 方向：外贸｜分类：外贸合规
- 收录：第 013 期（2026-11-19），额度核对日期见当期
- 网址：https://developer.trade.gov/

**网址**：https://developer.trade.gov/ ；接口 https://api.trade.gov/gateway/v1/consolidated_screening_list/search

**注册**：developer.trade.gov 注册账号，订阅 Data Services Platform APIs 后在个人页取得订阅密钥，免费

**额度**：官方页面注明密钥免费；限流数字以各 API 文档页和官方控制台为准

**用法**：GET 上述接口，带 name=客户名称&fuzzy_name=true 做模糊名称搜索，并附订阅密钥 YOUR_API_KEY

**Agent 适配**：REST + JSON，一次查商务部、国务院、财政部多份名单，适合做自动化合规初筛

**场景**：Agent 在接新客户询盘时，先筛一遍是否在美国出口限制名单上

**匹配度**：★★★★☆


[返回目录](../README.md)