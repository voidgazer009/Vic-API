# Google Cloud Text-to-Speech

> 自媒体配音｜多语种配音

- 方向：自媒体｜分类：自媒体配音
- 收录：第 013 期（2026-11-19），额度核对日期见当期
- 网址：https://cloud.google.com/text-to-speech/pricing

**网址**：https://cloud.google.com/text-to-speech/pricing ；文档 https://cloud.google.com/text-to-speech/docs

**注册**：需 Google Cloud 账号并启用计费，超出免费量才会扣费

**额度**：每月免费：Standard 与 WaveNet 各 400 万字符，Chirp 3: HD、Neural2、Studio 各 100 万字符；超出后 Standard 每百万字符 4 美元

**用法**：POST https://texttospeech.googleapis.com/v1/text:synthesize ，请求头 X-Goog-Api-Key: YOUR_API_KEY ，正文含 input、voice、audioConfig

**Agent 适配**：官方多语言 SDK 和 REST，可按语言和声线批量生成音频

**场景**：Agent 把短视频脚本转成多语种配音，发到全球账号

**匹配度**：★★★★☆


[返回目录](../README.md)