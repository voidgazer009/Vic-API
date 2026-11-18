# Azure AI Translator

> 外贸翻译｜每月 200 万字符

- 方向：外贸｜分类：外贸翻译
- 收录：第 012 期（2026-11-18），额度核对日期见当期
- 网址：https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator/

**网址**：https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator/ ；文档 https://learn.microsoft.com/azure/ai-services/translator/

**注册**：需 Azure 账号，创建 Translator 资源时选 F0 免费档

**额度**：F0 免费档每月 200 万字符（标准翻译与自定义翻译训练合计）

**用法**：POST https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en ，请求头 Ocp-Apim-Subscription-Key: YOUR_API_KEY ，正文为 JSON 文本数组

**Agent 适配**：REST + JSON，一次可传多段文本、多个目标语言，适合批量翻译询盘和产品描述

**场景**：Agent 把海外客户询盘译成中文，再把回复译回客户语言

**匹配度**：★★★★☆


[返回目录](../README.md)