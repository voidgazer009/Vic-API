# Cloudflare AI Gateway

> AI网关｜缓存限流与日志

- 方向：一人公司｜分类：AI网关
- 收录：第 012 期（2026-11-18），额度核对日期见当期
- 网址：https://developers.cloudflare.com/ai-gateway/reference/pricing/

**网址**：https://developers.cloudflare.com/ai-gateway/reference/pricing/

**注册**：Cloudflare 账号，控制台创建 Gateway

**额度**：核心功能免费（分析、缓存、限流）；Workers Free 日志总量 10 万条

**用法**：把 OpenAI 等模型的请求地址改成 https://gateway.ai.cloudflare.com/v1/ 开头的网关地址，其余不变

**Agent 适配**：一行改地址即可接入，为所有模型调用统一加缓存、限流与用量统计

**场景**：Agent 的重复提问走缓存省钱，并看清每个模型花了多少

**匹配度**：★★★★☆


[返回目录](../README.md)