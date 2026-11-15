# Slack API

> 一人公司协作｜Agent 的通知中枢

- 方向：一人公司｜分类：一人公司协作
- 收录：第 008 期（2026-11-14），额度核对日期见当期
- 网址：https://docs.slack.dev

**网址**：https://docs.slack.dev

**注册**：创建免费 Slack 工作区，在 api.slack.com/apps 新建 App 拿 Token

**额度**：官方限流页：发消息约每频道每秒 1 条；Web API 按方法分 Tier 1–4（每分钟 1+ / 20+ / 50+ / 100+ 次）；Events API 每小时 3 万次投递

**用法**：用 Bolt SDK 或 chat.postMessage / Incoming Webhook 发消息，Events API 收指令

**Agent 适配**：官方文档含 Slack MCP Server 与 Agent 接入页，可直接接 Cursor、Claude 等

**场景**：订单与物流异常告警、内容日报、让 Agent 在频道里接任务

**匹配度**：★★★★☆


[返回目录](../README.md)