# YouTube Data API

> 自媒体｜选题与数据分析

- 方向：自媒体｜分类：自媒体数据
- 收录：第 002 期（2026-11-08），额度核对日期见当期
- 网址：https://developers.google.com/youtube/v3

**网址**：https://developers.google.com/youtube/v3 ；配额说明 https://developers.google.com/youtube/v3/getting-started

**注册**：Google Cloud 控制台建项目 → 启用 YouTube Data API v3 → 创建 API Key（上传/评论需 OAuth）

**额度**：默认每天 100 次 search.list、100 次 videos.insert，其余接口合计 10,000 单位/天；读取一般 1 单位，写入一般 50 单位；可申请提额

**用法**：GET https://www.googleapis.com/youtube/v3/search?part=snippet&q=…&key=KEY

**Agent 适配**：官方各语言客户端库，Agent 可自动拉热门视频、标题、评论做分析

**场景**：找爆款选题、分析竞品频道、自动上传视频和设缩略图

**匹配度**：★★★★☆


[返回目录](../README.md)