# National Weather Service API

> 物流天气｜美国官方天气

- 方向：物流｜分类：物流天气
- 收录：第 014 期（2026-11-20），额度核对日期见当期
- 网址：https://www.weather.gov/documentation/services-web-api

**网址**：https://www.weather.gov/documentation/services-web-api ；接口 https://api.weather.gov/

**注册**：无需注册，无需 Key，请求时需带自定义 User-Agent 标识

**额度**：官方页面写明免费、可用于任何用途；限流数字不公开，页面称对常规使用「足够宽松」，超限会报错并通常在约 5 秒后可重试

**用法**：先 GET https://api.weather.gov/points/38.8894,-77.0352 取得网格，再请求返回的 forecast 地址

**Agent 适配**：开放数据、REST + JSON，无需密钥，Agent 可直接调用

**场景**：Agent 为美国港口和内陆运输提前预警暴风雪、飓风等天气延误

**匹配度**：★★★☆☆


[返回目录](../README.md)