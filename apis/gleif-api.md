# GLEIF API

> 外贸合规｜全球企业 LEI 身份库

- 方向：外贸｜分类：外贸合规
- 收录：第 015 期（2026-11-21），额度核对日期见当期
- 网址：https://www.gleif.org/en/lei-data/gleif-api

**网址**：https://www.gleif.org/en/lei-data/gleif-api ；文档 https://api.gleif.org/docs

**注册**：无需注册，无需 Key，直接调用公开接口

**额度**：官方文档写明限流为每个用户每分钟 60 次请求，所有用户一致

**用法**：GET https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]=公司名

**Agent 适配**：REST + JSON，支持名称模糊搜索，可按 LEI 查母子公司股权关系

**场景**：Agent 在签约前核对海外买家的法定名称、注册地和母公司，补全背调

**匹配度**：★★★★☆


[返回目录](../README.md)