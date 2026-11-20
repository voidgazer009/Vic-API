# currencylayer

> 外贸汇率｜轻量汇率与历史价

- 方向：外贸｜分类：外贸汇率
- 收录：第 014 期（2026-11-20），额度核对日期见当期
- 网址：https://currencylayer.com/product

**网址**：https://currencylayer.com/product ；文档 https://currencylayer.com/documentation

**注册**：官网点 Get Free API Key，邮箱注册后获得 Access Key

**额度**：免费版页面写明 100 次 API 调用、每日更新、含历史汇率、仅限非商业使用；商业使用需付费 Basic 档（$14.99/月，最多 10,000 次请求）

**用法**：GET https://api.currencylayer.com/live?access_key=YOUR_API_KEY&currencies=EUR,GBP,CNY

**Agent 适配**：REST + JSON，一次返回多币种；免费额度小，适合给 Agent 做每日汇率快照

**场景**：Agent 生成外贸报价单时，按当天汇率换算多币种价格

**匹配度**：★★★☆☆


[返回目录](../README.md)