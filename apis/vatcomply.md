# VATcomply

> 外贸合规｜欧盟增值税与汇率

- 方向：外贸｜分类：外贸合规
- 收录：第 011 期（2026-11-17），额度核对日期见当期
- 网址：https://www.vatcomply.com

**网址**：https://www.vatcomply.com ；接口 https://api.vatcomply.com

**注册**：无需注册，无需 Key

**额度**：无需 Key；按 IP 限速每秒 2 次请求

**用法**：GET https://api.vatcomply.com/vat?vat_number=BE0123456789 校验欧盟增值税号；/vat_rates 查各国税率；/rates 查欧洲央行汇率

**Agent 适配**：纯 GET + JSON，Agent 可在报价或开票前自动校验欧盟客户税号

**场景**：向欧盟客户开发票前，让 Agent 校验对方 VAT 号并查当地税率

**匹配度**：★★★★☆


[返回目录](../README.md)