# Companies House API

> 外贸企业背调｜英国公司官方登记

- 方向：外贸｜分类：外贸企业背调
- 收录：第 014 期（2026-11-20），额度核对日期见当期
- 网址：https://developer-specs.company-information.service.gov.uk/

**网址**：https://developer-specs.company-information.service.gov.uk/ ；开发者中心 https://developer.company-information.service.gov.uk/

**注册**：在 Companies House 开发者中心注册账号，创建 API Key 类型的应用即可获得密钥

**额度**：官方限流指南写明每个应用每五分钟窗口最多 600 次请求；需要更高额度可联系官方申请

**用法**：GET https://api.company-information.service.gov.uk/search/companies?q=公司名 ，用 YOUR_API_KEY 作为基本认证的用户名

**Agent 适配**：REST + JSON，可查公司状态、董事、注册地址，适合做英国买家的自动背调

**场景**：Agent 收到英国客户询盘后，先核实公司是否真实存在、是否仍在营业

**匹配度**：★★★★☆


[返回目录](../README.md)