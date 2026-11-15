# Cloudflare Workers AI

> 边缘推理｜每日免费推理

- 方向：一人公司｜分类：边缘推理
- 收录：第 002 期（2026-11-08），额度核对日期见当期
- 网址：https://developers.cloudflare.com/workers-ai

**网址**：https://developers.cloudflare.com/workers-ai ；定价 https://developers.cloudflare.com/workers-ai/platform/pricing/

**注册**：Cloudflare 账号（免费 Workers 计划即可）→ 控制台 AI → Workers AI → 创建 API Token，记下 Account ID

**额度**：免费 10,000 Neurons/天，每天 00:00 UTC 重置；超出需 Workers Paid，$0.011/1,000 Neurons。部分新模型（如 Kimi K2.6、GLM 5.x、DeepSeek V4）需付费方式才能调用

**用法**：OpenAI 兼容端点 https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/v1 ，或 Workers 里 env.AI.run()

**Agent 适配**：函数调用、JSON 模式、官方 MCP 服务器与 Agents SDK；同时有 LLM、向量、Whisper 语音、FLUX 绘图

**场景**：便宜的批量文本分类/摘要、给知识库做向量、短视频语音转字幕

**匹配度**：★★★★☆


[返回目录](../README.md)