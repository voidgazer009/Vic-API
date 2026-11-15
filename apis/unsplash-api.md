# Unsplash API

> 自媒体素材｜高质量免版权图库

- 方向：自媒体｜分类：自媒体素材
- 收录：第 003 期（2026-11-09），额度核对日期见当期
- 网址：https://unsplash.com/developers

**网址**：https://unsplash.com/developers ；文档 https://unsplash.com/documentation

**注册**：unsplash.com 注册开发者账号 → Your apps → New Application 拿 Access Key

**额度**：新应用为 Demo 模式，50 次请求/小时；申请 Production 获批后 1,000 次/小时；只统计 api.unsplash.com 的 JSON 请求，图片文件请求不计；使用须按规范标注摄影师和 Unsplash

**用法**：GET https://api.unsplash.com/search/photos?query=logistics ，头部 Authorization: Client-ID {AccessKey}

**Agent 适配**：官方 SDK，响应带动态裁剪参数（宽高、格式）和 BlurHash；返回摄影师信息便于自动署名

**场景**：Agent 写完文章/公众号自动配图；给产品页和社媒帖找背景图

**匹配度**：★★★☆☆（与 Pexels 互补）


[返回目录](../README.md)