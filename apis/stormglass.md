# Stormglass

> 物流海运天气｜全球海浪与风速

- 方向：物流｜分类：物流海运天气
- 收录：第 014 期（2026-11-20），额度核对日期见当期
- 网址：https://stormglass.io/pricing/

**网址**：https://stormglass.io/ ；定价 https://stormglass.io/pricing/

**注册**：官网点 Try for free 注册后在控制台获得 API Key

**额度**：免费档每天 10 次请求，含全部天气参数，不提供支持，且不可商用；付费 Small 档 €19/月，每天 500 次

**用法**：GET https://api.stormglass.io/v2/weather/point?lat=22.3&lng=114.2&params=waveHeight,windSpeed ，请求头 Authorization: YOUR_API_KEY

**Agent 适配**：REST + JSON，适合按航线坐标查浪高风速；免费次数少，只宜做个人测试

**场景**：Agent 评估海运航线上的海况，辅助判断船期是否可能延误

**匹配度**：★★★☆☆


[返回目录](../README.md)