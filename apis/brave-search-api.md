# Brave Search API

> 搜索｜Agent 专用搜索

- 方向：一人公司｜分类：搜索
- 收录：第 003 期（2026-11-09），额度核对日期见当期
- 网址：https://brave.com/search/api

**网址**：https://brave.com/search/api ；定价 https://api-dashboard.search.brave.com/documentation/pricing

**注册**：api-dashboard.search.brave.com 注册 → 订阅 Search 计划 → 生成 API Key（是否需绑定支付方式以注册页为准）

**额度**：Search 计划每月含 $5 免费额度，按 $5/千次请求计，约合 1,000 次；容量 50 次/秒。Answers 另计 $4/千次查询 + token 费

**用法**：GET https://api.search.brave.com/res/v1/web/search?q=关键词 ，请求头带 X-Subscription-Token ；LLM Context 接口直接返回适合喂给模型的片段

**Agent 适配**：提供 LLM Context（给 Agent 的搜索结果）、Answers（带引用答案）、新闻/图片/视频/地点搜索；官方有 MCP 服务器（GitHub brave/brave-search-mcp-server）

**场景**：Agent 联网查行业新闻、核对客户公司信息、给自媒体选题找热点

**匹配度**：★★★★☆


[返回目录](../README.md)