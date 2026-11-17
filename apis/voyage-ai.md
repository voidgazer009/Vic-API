# Voyage AI

> AI向量｜嵌入与重排模型

- 方向：一人公司｜分类：AI向量
- 收录：第 011 期（2026-11-17），额度核对日期见当期
- 网址：https://docs.voyageai.com/docs/pricing

**网址**：https://docs.voyageai.com/docs/pricing ；官网 https://www.voyageai.com

**注册**：官网注册后在控制台创建 API Key

**额度**：每个账号 voyage-4-large、voyage-4、voyage-4-lite 等前 2 亿 token 免费；voyage-finance-2 等前 5,000 万 token 免费；重排模型前 2 亿 token 免费；多模态前 2 亿文本 token 加 1,500 亿像素免费

**用法**：POST https://api.voyageai.com/v1/embeddings ，Header 带 Authorization: Bearer YOUR_API_KEY，body 里写 model 和 input

**Agent 适配**：给 Agent 记忆和 RAG 做向量检索，配套 Python 客户端

**场景**：把客户邮件、产品资料向量化，让 Agent 按语义检索回复

**匹配度**：★★★★★


[返回目录](../README.md)