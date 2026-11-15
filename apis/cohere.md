# Cohere

> AI 模型｜Rerank 提升 RAG

- 方向：一人公司｜分类：AI模型
- 收录：第 003 期（2026-11-09），额度核对日期见当期
- 网址：https://cohere.com

**网址**：https://cohere.com ；限额 https://docs.cohere.com/docs/rate-limits

**注册**：dashboard.cohere.com 注册 → API keys 页面创建 Trial（评估）Key

**额度**：Trial Key 免费但有限：每月 1,000 次 API 调用；Chat 各模型 20 次/分钟；Embed 2,000 条输入/分钟；Rerank 10 次/分钟；语音转写 5 次/分钟；生产用需付费 Key

**用法**：Python/JS SDK 或 POST https://api.cohere.com/v2/rerank 、/v2/embed 、/v2/chat

**Agent 适配**：Chat 支持工具调用与 RAG 引用；Rerank 可对搜索结果二次排序；Embed 做语义检索；有 LangChain、LlamaIndex 集成，也可经 OpenRouter 调用

**场景**：Brave/Exa 搜出一堆结果后用 Rerank 选最相关 5 条；给客户问答库做向量检索

**匹配度**：★★★★☆（1000 次/月适合评估和小项目）


[返回目录](../README.md)