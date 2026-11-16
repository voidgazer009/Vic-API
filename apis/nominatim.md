# Nominatim

> 物流地理｜地址转坐标

- 方向：物流｜分类：物流地理编码
- 收录：第 010 期（2026-11-16），额度核对日期见当期
- 网址：https://nominatim.org

**网址**：https://nominatim.org ；公共服务政策 https://operations.osmfoundation.org/policies/nominatim/

**注册**：公共服务无需 Key，但必须带能识别应用的 User-Agent 或 Referer

**额度**：公共服务最多每秒 1 次请求；定期运行的脚本限每分钟 4 次；结果必须缓存；禁止自动补全和网格式批量查询

**用法**：GET https://nominatim.openstreetmap.org/search?q=Rotterdam&format=json

**Agent 适配**：适合偶尔把地址转坐标；批量需求请自建或换付费服务

**场景**：把客户发来的收货地址转成坐标，再接路线或天气 API

**匹配度**：★★★☆☆


[返回目录](../README.md)