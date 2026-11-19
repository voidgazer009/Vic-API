# UK Trade Tariff API

> 外贸关税｜英国官方关税数据

- 方向：外贸｜分类：外贸关税
- 收录：第 013 期（2026-11-19），额度核对日期见当期
- 网址：https://docs.trade-tariff.service.gov.uk/

**网址**：https://docs.trade-tariff.service.gov.uk/ ；开发者门户 https://hub.trade-tariff.service.gov.uk/

**注册**：基础查询无需注册；在开发者门户注册后可创建 API Key，并使用 OAuth 2.0 令牌

**额度**：开发者门户注册后每个 Key 每分钟 750 次，一个组织最多 3 个有效 Key；未认证访问的上限正由每分钟 500 次逐步下调，官方公告预计降到每分钟 50 次（2026-11-30 前完成）

**用法**：GET https://www.trade-tariff.service.gov.uk/api/v2/commodities/0101210000 ，返回商品编码、关税与进出口措施 JSON；带 Key 时按官方文档使用 api.trade-tariff.service.gov.uk 并附 Bearer 令牌

**Agent 适配**：官方 GitHub 提供 MCP 服务器（trade-tariff/mcp），含商品编码查询和自然语言归类搜索

**场景**：Agent 为英国客户报价前，自动查 HS 编码对应的关税和进口限制

**匹配度**：★★★★☆


[返回目录](../README.md)