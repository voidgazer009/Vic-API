# AISstream

> 物流船舶｜全球船舶 AIS 实时流

- 方向：物流｜分类：物流船舶AIS
- 收录：第 010 期（2026-11-16），额度核对日期见当期
- 网址：https://aisstream.io

**网址**：https://aisstream.io ；文档 https://aisstream.io/documentation

**注册**：账号页生成 API Key（官方文档未写明套餐收费）

**额度**：每账号 3 个订阅连接、每 IP 3 个连接；单个订阅最多 200 个 MMSI；订阅更新每连接每秒 1 次；官方说明不提供 SLA

**用法**：WebSocket 连接 wss://stream.aisstream.io/v0/stream，3 秒内发送含 APIKey 与 BoundingBoxes 的订阅 JSON

**Agent 适配**：需在服务器端运行，不允许浏览器直连；可用 MMSI 过滤只看自己的船

**场景**：盯着货柜船位置与靠港动态，提前告知客户到港时间

**匹配度**：★★★★☆


[返回目录](../README.md)