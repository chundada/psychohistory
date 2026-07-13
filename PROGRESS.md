---
tags: [psychohistory, core]
type: "progress"
---

# 📊 Psychohistory - 项目进度追踪

> 最后更新: 2026-07-13
> ✅ 已完成 4 个系列 · 共 142 个技能文件

---

## 🗺️ 路线图总览

```mermaid
gantt
    title Psychohistory 蒸馏路线图
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    
    section Phase 1 - 架构搭建
    设计蒸馏流水线           :done, 2026-07-13, 1d
    创建提取器+模板          :done, 2026-07-13, 1d
    创建 GitHub 仓库         :done, 2026-07-13, 1d
    
    section Phase 2 - Game Theory ✅
    下载字幕/转录文本        :done, 2026-07-13, 1d
    检索式提取 (7路)         :done, 2026-07-13, 1d
    四重验证 + 筛选          :done, 2026-07-13, 1d
    RIA++ 构造 (52 Skills)   :done, 2026-07-13, 1d
    交付 (INDEX/DIGEST/QUICK) :done, 2026-07-13, 1d
    
    section Phase 3 - Secret History ✅
    检索式提取 (7路)         :done, 2026-07-13, 1d
    四重验证 + 筛选          :done, 2026-07-13, 1d
    RIA 构造 (45 Skills)     :done, 2026-07-13, 1d
    交付 (_INDEX.md)         :done, 2026-07-13, 1d
    
    section Phase 4 - Geo-Strategy ✅
    检索式提取 (7路)         :done, 2026-07-13, 1d
    四重验证 + 筛选          :done, 2026-07-13, 1d
    RIA 构造 (35 Skills)     :done, 2026-07-13, 1d
    交付                     :done, 2026-07-13, 1d
    
    section Phase 5 - Interview ✅
    检索式提取               :done, 2026-07-13, 1d
    RIA 构造 (10 Skills)     :done, 2026-07-13, 1d

    section Phase 6 - 扩展 (待处理)
    Civilization 系列(59集)  :2026-07-20, 7d
    Great Books 系列(13集)   :2026-07-27, 3d
    Dante 系列(12集)         :2026-08-01, 3d
```

---

## ✅ 已完成

### 📋 架构设计

- [x] `SPEC.md` — 检索式提取架构设计
- [x] `methodology/` — 8 篇详细流水线 SOP
- [x] `extractors/` — 7 个检索式提取器 + 信号表
- [x] `templates/` — 4 个输出模板

### 🎮 Series 1: Game Theory — 29 集 ✅

| 阶段 | 产出 | 状态 |
|---|---|---|
| Stage 0: 系列理解 | 29 集清单 + 主题弧划分 | ✅ |
| Stage 1: 检索式提取 | 7 路提取器 → 81+ 方法论候选 | ✅ |
| Stage 1.5: 四重验证 | 36 HIGH + 14 MEDIUM + 1 REJECT + 4 参考 | ✅ |
| Stage 2: RIA++ 构造 | **52 个 SKILL.md**，完整 R/I/A1/A2/E/B 六段格式 | ✅ |
| Stage 3-5: 交付 | INDEX.md + DIGEST.md + QUICK_START.md | ✅ |
| 技能位置 | `skills/gt-*.md`（已同步到根目录） | ✅ |

### 📜 Series 2: Secret History — 27 集 ✅

| 阶段 | 产出 | 状态 |
|---|---|---|
| 检索式提取 | 7 路提取器 → 92 候选 | ✅ |
| 蒸馏 | **45 个 SKILL.md**，RIA 四段格式（R/I/A/B） | ✅ |
| 交付 | `series/secret-history/_INDEX.md` | ✅ |
| 技能位置 | `skills/sh-*.md` + `series/secret-history/skills/` | ✅ |

### 🗺️ Series 3: Geo-Strategy — 19 集 ✅

| 阶段 | 产出 | 状态 |
|---|---|---|
| 检索式提取 | 7 路提取器 → 77 候选 | ✅ |
| 蒸馏 | **35 个 SKILL.md**，RIA 四段格式（R/I/A/B） | ✅ |
| 技能位置 | `series/geo-strategy/skills/` | ⚠️ 未同步到根目录 skills/ |

### 🎙️ Series 4: Interview (Jang Let's Talk) ✅

| 阶段 | 产出 | 状态 |
|---|---|---|
| 检索式提取 | 提取 | ✅ |
| 蒸馏 | **10 个 SKILL.md**，RIA 格式 | ✅ |
| 技能位置 | `skills/interview-*.md`（已同步到根目录） | ✅ |

### 📦 技能汇总

| 系列 | 前缀 | 数量 | 位置 | 格式 |
|---|---|---|---|---|
| Game Theory | `gt-` | 52 | `skills/` | RIA++ 六段 |
| Secret History | `sh-` | 45 | `skills/` + `series/secret-history/skills/` | RIA 四段 |
| Geo-Strategy | `gs-` | 35 | `series/geo-strategy/skills/` | RIA 四段 |
| Interview | `interview-` | 10 | `skills/` | RIA 四段 |
| **合计** | | **142** | | |

---

## 🟡 已知问题

| 问题 | 严重性 | 说明 |
|---|---|---|
| gs- 未同步到根目录 | 🟡 中 | Geo-Strategy 35 个技能仅在 `series/geo-strategy/skills/`，CLAUDE.md 已更新路径说明 |
| RIA++ 格式不一致 | 🟡 中 | GT 用六段（R/I/A1/A2/E/B），SH/GS/Interview 用四段（R/I/A/B）。功能不受影响，统一为后续优化项 |
| SH/GS 缺 verified.md | 🟡 低 | Secret History 和 Interview 系列未检出验证文件 |
| INDEX.md/QUICK_START/DIGEST 未覆盖新系列 | 🟡 中 | 当前仍只索引 Game Theory。后续需要扩展 |

---

## 🟢 下一个系列待处理

| 系列 | 集数 | 预计 Skills | 优先级 |
|---|---|---|---|
| 📜 **Civilization** | **59** | 25-35 | ⭐⭐⭐ 最高 |
| 📚 **Great Books** | **13** | 8-12 | ⭐⭐ |
| 🔥 **Dante** | **12** | 8-10 | ⭐ |

---

## 📌 方法论版本记录

| 版本 | 日期 | 变更 |
|------|------|------|
| **v5.0** | 2026-07-13 | 全面审计：更新项目状态反映 4 个系列 142 个技能已完成。更新 PROGRESS.md、CLAUDE.md |
| v4.0 | 2026-07-13 | Game Theory Pilot 完整验证。新增 QUICK_START.md |
| v3.0 | 2026-07-13 | 检索式提取替换两阶段摘要 |
| v2.0 | 2026-07-13 | 初始：两阶段摘要提取架构 |