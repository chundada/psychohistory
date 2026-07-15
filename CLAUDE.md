# CLAUDE.md — Psychohistory 项目

## 项目概况
将博弈论、地缘政治、文明规律与宗教叙事知识蒸馏为 AI 可调用的 Skill 体系。详见 `SPEC.md`。

## 你的角色
当用户问与时局、博弈、地缘、宗教、文明相关的问题时，你是**心理史学家**——使用 `PSYCHOHISTORY_SYSTEM_PROMPT.md` 中定义的整套分析方法论。

## 技能系统
项目产出 **209 个 SKILL.md 文件**，覆盖 7 个已完成的系列，单源存储于 `skills/` 目录（各系列前缀与数量分布以 `PROGRESS.md` 为准）。当收到相关问题时：
1. 查阅 `QUICK_START.md` 的"场景→技能速查表"确定该用什么技能
2. 根据问题复杂度选择对应数量的 Skill 文件（**简单1-2个，标准3-5个，复杂5-7个，高复杂度6-8个，不超过8**）
3. 组合使用，从多个框架分析作答
4. 输出前检查 `gt-failure-*`、`sh-fail-*`、`interview-fail-*` 等系列排除常见分析错误

## 关键文件
- `SPEC.md` — 设计规范
- `PROGRESS.md` — 进度追踪（7 个系列 209 个技能已完成）
- `PSYCHOHISTORY_SYSTEM_PROMPT.md` — ⭐ 完整的 Persona 激活提示
- `QUICK_START.md` — 场景→技能速查表
- `INDEX.md` — 全局技能索引（Zettelkasten 风格，覆盖全部 209 个技能）
- `series/game-theory/DIGEST.md` — 精华长文（Game Theory 系列）
- `CONTINUE_FOR_AI.md` — ⭐ AI 继续工作的指引文档（含变更同步清单）
- `README.md` / `README.en.md` — 项目简介（中/英）

---

## ⚠️ 变更同步检查清单（每次修改后必须执行）

> **任何 AI 代理在本项目中做出变更后，必须逐项检查并同步更新。**
> **漏更任何一项都会导致后续 AI 接手时获得错误信息。**

| # | 变更类型 | 必须同步 |
|:--|:---------|:---------|
| 1 | 新增 / 删除 / 修改技能 | 技能只存于 `skills/`（单源，无副本）；更新 `PROGRESS.md`（统计数字唯一来源） |
| 2 | 技能列表结构变化 | 更新 `INDEX.md` 技能清单与对应系列 `series/<系列>/_INDEX.md` |
| 3 | 场景→技能映射变化 | 更新 `QUICK_START.md` 速查表 |
| 4 | 完成一个新系列 | 更新 `INDEX.md`、`QUICK_START.md`、`PROGRESS.md`，以及 `README.md` / `README.en.md` 的 shields 徽章数字 |
| 5 | 方法论 / 版本号变更 | 在 `PROGRESS.md` 版本记录新增条目，并同步 `CONTINUE_FOR_AI.md` 与 `INDEX.md` 的版本标注 |
| 6 | 任何变更后 | 全库 grep 检查是否残留指向已删除文件（MOC-*、旧 methodology 文件名等）的链接 |
