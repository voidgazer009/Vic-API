# World Bank Indicators API

> 外贸数据｜全球经济指标库

- 方向：外贸｜分类：外贸数据
- 收录：第 010 期（2026-11-16），额度核对日期见当期
- 网址：https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation

**网址**：https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation ；接口 https://api.worldbank.org/v2/country

**注册**：无需注册，无需 Key，直接 GET 调用

**额度**：以官方控制台为准（实测无 Key 即可返回 JSON，官方文档未写明具体请求上限）

**用法**：GET https://api.worldbank.org/v2/country/CN/indicator/NE.EXP.GNFS.CD?format=json 返回中国货物与服务出口额

**Agent 适配**：纯 REST + JSON，Agent 可直接按国家和指标代码拼 URL，无需认证流程

**场景**：开发新市场前，让 Agent 对比各国进口规模、GDP、人口，生成选市场简报

**匹配度**：★★★★☆


[返回目录](../README.md)