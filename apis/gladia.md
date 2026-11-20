# Gladia

> 自媒体语音转写｜多语言转写与说话人分离

- 方向：自媒体｜分类：自媒体语音转写
- 收录：第 014 期（2026-11-20），额度核对日期见当期
- 网址：https://www.gladia.io/pricing

**网址**：https://www.gladia.io/ ；定价 https://www.gladia.io/pricing

**注册**：官网注册账号，在控制台获取 API Key

**额度**：自助档页面写明新用户送 €50 免费额度；之后按量付费，异步转写起价每小时 €0.16；支持 100 多种语言和说话人分离

**用法**：先 POST https://api.gladia.io/v2/upload 上传音频，再 POST https://api.gladia.io/v2/pre-recorded 发起转写，请求头 x-gladia-key: YOUR_API_KEY

**Agent 适配**：REST + JSON，异步任务模式，适合批量处理访谈和播客

**场景**：Agent 把多语言采访音频转成字幕和文字稿，用于全球账号发布

**匹配度**：★★★★☆


[返回目录](../README.md)