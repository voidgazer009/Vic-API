# Notion API

> 一人公司｜Agent 的数据库与知识库

- 方向：一人公司｜分类：一人公司效率
- 收录：第 002 期（2026-11-08），额度核对日期见当期
- 网址：https://developers.notion.com

**网址**：https://developers.notion.com ；限额 https://developers.notion.com/reference/request-limits

**注册**：notion.so/developers 新建 Integration → 拿 Token → 在页面里把该 Integration 加入

**额度**：API 免费；非 Business/Enterprise 工作区每个连接 180 次/分钟（平均 3 次/秒），查询数据源约 3 次/秒；单次请求最多 1000 个块、500KB

**用法**：POST https://api.notion.com/v1/pages ，官方 JS SDK 自动重试 429

**Agent 适配**：官方 MCP、Webhooks、Agents 接口

**场景**：Agent 自动写客户 CRM、内容日历、订单台账，人看 Notion 就行

**匹配度**：★★★★★


[返回目录](../README.md)