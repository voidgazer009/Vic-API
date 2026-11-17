# OpenSky Network API

> 物流航空｜全球飞机实时位置

- 方向：物流｜分类：物流航空
- 收录：第 011 期（2026-11-17），额度核对日期见当期
- 网址：https://openskynetwork.github.io/opensky-api/rest.html

**网址**：https://openskynetwork.github.io/opensky-api/rest.html ；接口 https://opensky-network.org/api/states/all

**注册**：匿名可调用；登录后在账户页创建 API 客户端，用 OAuth2 取令牌可获更高额度

**额度**：匿名每天 400 积分；标准注册用户每天 4,000 积分；状态、轨迹、航班三类接口各自独立计额

**用法**：GET https://opensky-network.org/api/states/all?icao24=3c6444 查指定飞机当前状态

**Agent 适配**：JSON 返回，注册档需 OAuth2 客户端凭证，令牌 30 分钟过期，Agent 需自动续期

**场景**：追踪空运货机位置，估算到港时间并自动通知客户

**匹配度**：★★★☆☆


[返回目录](../README.md)