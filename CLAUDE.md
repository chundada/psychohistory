# CLAUDE.md — Psychohistory 项目

## 项目概况
将博弈论、地缘政治、文明规律与宗教叙事知识蒸馏为 AI 可调用的 Skill 体系。详见 `SPEC.md`。

## 你的角色
当用户问与时局、博弈、地缘、宗教、文明相关的问题时，你是**心理史学家**——使用 `PSYCHOHISTORY_SYSTEM_PROMPT.md` 中定义的整套分析方法论。

## 技能系统
项目产出 **209 个 SKILL.md 文件**，分布在 7 个已完成的系列中。当收到相关问题时：
1. 查阅 `QUICK_START.md` 的"场景→技能速查表"确定该用什么技能
2. 根据问题复杂度选择对应数量的 Skill 文件（**简单1-2个，标准3-5个，复杂5-7个，高复杂度6-8个，不超过8**）
3. 组合使用，从多个框架分析作答
4. 输出前检查 `gt-failure-*`、`sh-fail-*`、`interview-fail-*` 等系列排除常见分析错误

### 技能文件位置

| 位置 | 内容 |
|---|---|
| `skills/ph-origin-*.md` | Psychohistory Origin 系列（6 个，RIA 四段格式） |
| `skills/gt-*.md` | Game Theory 系列（52 个，RIA++ 六段格式） |
| `skills/sh-*.md` | Secret History 系列（46 个，RIA 四段格式） |
| `skills/gs-*.md` | Geo-Strategy 系列（35 个，RIA 四段格式） |
| `skills/interview-*.md` | Interview 系列（10 个，RIA 格式） |
| `skills/civ-*.md` | Civilization 系列（50 个，RIA 四段格式） |
| `skills/gb-*.md` | Great Books 系列（10 个，RIA 四段格式） |

## 关键文件
- `SPEC.md` — 设计规范
- `PROGRESS.md` — 进度追踪（7 个系列 209 个技能已完成）
- `PSYCHOHISTORY_SYSTEM_PROMPT.md` — ⭐ 完整的 Persona 激活提示
- `QUICK_START.md` — 场景→技能速查表
- `INDEX.md` — 全局技能索引（Zettelkasten 风格，覆盖全部 209 个技能）
- `DIGEST.md` — 精华长文（Game Theory 系列）
- `CONTINUE_FOR_AI.md` — ⭐ AI 继续工作的指引文档（含变更同步清单）
- `README.md` / `README.en.md` — 项目简介（中/英）

---

## ⚠️ 变更同步检查清单（每次修改后必须执行）

> **任何 AI 代理在本项目中做出变更后，必须按下表逐项检查并同步更新。**
> **漏更任何一项都会导致后续 AI 接手时获得错误信息。**

### 场景 A：新增 / 删除 / 修改 Skill 文件

| 序号 | 必须更新的文件 | 更新内容 |
|:-----|:--------------|:---------|
| 1 | `skills/` 目录 | 新增/修改 Skill 文件本体 |
| 2 | `series/<对应系列>/skills/` | 同步到系列原始位置（保持双向一致） |
| 3 | `INDEX.md` | 更新技能总数、技能列表、触发场景映射 |
| 4 | `QUICK_START.md` | 更新开篇统计数字、场景→技能速查表 |
| 5 | `PROGRESS.md` | 更新技能总数、系列状态、版本记录 |
| 6 | `README.md` | 更新徽章数字、系列分布表、仓库结构注释 |
| 7 | `README.en.md` | 同步更新英文版徽章和统计数字 |
| 8 | `CLAUDE.md`（本文件） | 更新技能总数、技能文件位置表 |
| 9 | `CONTINUE_FOR_AI.md` | 更新已完成系列技能数、仓库结构注释 |
| 10 | `MOC-系列目录.md` | 更新对应系列的状态和技能数 |
| 11 | `MOC-心理史学总览.md` | 更新核心统计表中的技能总数 |
| 12 | 对应系列的 `_INDEX.md` | 更新系列内技能列表 |

### 场景 B：完成一个新系列

除场景 A 全部项之外，还需更新：

| 序号 | 必须更新的文件 | 更新内容 |
|:-----|:--------------|:---------|
| 13 | `MOC-系列目录.md` | 系列状态从"待处理"改为"已完成"，注明技能数 |
| 14 | `MOC-<系列名>.md` | 如有对应 MOC，更新状态为已完成 |
| 15 | `CONTINUE_FOR_AI.md` | 新增系列完成记录，更新下一步计划 |
| 16 | `PROGRESS.md` | 新增版本记录，更新已完成系列数 |
| 17 | `.gitignore` | 检查是否有新的临时文件类型需排除 |

### 场景 C：方法论 / 版本号变更

| 序号 | 必须更新的文件 | 更新内容 |
|:-----|:--------------|:---------|
| 18 | `PROGRESS.md` | 新增版本记录条目 |
| 19 | `CONTINUE_FOR_AI.md` | 更新方法论版本号 |
| 20 | `MOC-心理史学总览.md` | 更新核心方法和版本号 |
| 21 | `MOC-核心方法论.md` | 更新当前版本号 |
| 22 | `methodology/00-overview.md` | 更新文档底部版本标注 |
| 23 | `INDEX.md` | 更新最后更新版本号 |
| 24 | `CLAUDE.md`（本文件） | 检查是否需要同步 |

### 当前统计数据快照（2026-07-15 v9.2）

> 以下数字必须全项目一致。如发现不一致，以 `PROGRESS.md` 为准。

| 指标 | 值 |
|:-----|:---|
| 技能总数 | **209** |
| 已完成系列数 | **7** |
| Origin 技能数 | 6 |
| Game Theory 技能数 | 52 |
| Secret History 技能数 | 46 |
| Geo-Strategy 技能数 | 35 |
| Interview 技能数 | 10 |
| Civilization 技能数 | 50 |
| Great Books 技能数 | 10 |
| 方法论版本 | v9.2 |
