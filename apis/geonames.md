# GeoNames

> 物流地名数据｜全球地名与邮编库

- 方向：物流｜分类：物流地名数据
- 收录：第 013 期（2026-11-19），额度核对日期见当期
- 网址：https://www.geonames.org/export/

**网址**：https://www.geonames.org/export/ ；文档 https://www.geonames.org/export/web-services.html

**注册**：创建账号，请求中用 username 参数标识应用

**额度**：免费，每个 username 每天 10,000 点数、每小时 1,000 点数；数据采用 CC-BY 许可，允许商用

**用法**：GET https://secure.geonames.org/searchJSON?q=Hamburg&maxRows=5&username=YOUR_USERNAME

**Agent 适配**：REST + JSON，另有每日更新的全量地名文本和邮编数据可下载

**场景**：Agent 校验港口城市名与国家，补全收货地址的邮编和时区

**匹配度**：★★★★☆


[返回目录](../README.md)