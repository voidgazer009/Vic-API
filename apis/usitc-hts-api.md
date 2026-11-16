# USITC HTS API

> 外贸关税｜美国关税税则查询

- 方向：外贸｜分类：外贸关税
- 收录：第 010 期（2026-11-16），额度核对日期见当期
- 网址：https://hts.usitc.gov

**网址**：https://hts.usitc.gov ；接口 https://hts.usitc.gov/reststop/search

**注册**：无需注册，无需 Key

**额度**：以官方控制台为准（实测无 Key 可用，官方未公布具体上限）

**用法**：GET https://hts.usitc.gov/reststop/search?keyword=bicycle 按关键词返回 HTS 编码、税率与描述

**Agent 适配**：JSON 返回，可让 Agent 先把产品描述转成关键词，再回查 HS 编码和税率

**场景**：对美报价前自动查产品税号与关税，写进报价单

**匹配度**：★★★★☆


[返回目录](../README.md)