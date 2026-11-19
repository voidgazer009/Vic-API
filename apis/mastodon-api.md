# Mastodon API

> 自媒体发布｜联邦社交平台发帖

- 方向：自媒体｜分类：自媒体发布
- 收录：第 013 期（2026-11-19），额度核对日期见当期
- 网址：https://docs.joinmastodon.org/api/rate-limits/

**网址**：https://docs.joinmastodon.org/api/rate-limits/ ；文档 https://docs.joinmastodon.org/api/

**注册**：在任一 Mastodon 实例注册账号，到「偏好设置 → 开发」创建应用取得访问令牌

**额度**：免费；默认每个账号和每个 IP 5 分钟内各 300 次请求，上传媒体 30 分钟内 30 次，删帖 30 分钟内 30 次

**用法**：POST https://你的实例域名/api/v1/statuses ，请求头 Authorization: Bearer YOUR_API_KEY ，表单字段 status

**Agent 适配**：标准 REST + OAuth，限流信息在响应头 X-RateLimit-* 中返回，便于 Agent 自控节奏

**场景**：Agent 把当天选题自动发到海外 Mastodon 账号，并附图和链接

**匹配度**：★★★☆☆


[返回目录](../README.md)