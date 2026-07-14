---
tags: [psychohistory, moc, methodology]
created: 2026-07-13
status: live
---

# MOC - 核心方法论

> 心理史学的核心蒸馏流水线：从原始视频字幕到可调用 AI Skill 的 6 个阶段。

---

## 方法论概览

本项目的方法论经历了两次迭代：
- **v2.0**：两阶段摘要提取（旧方案 —— 1000:1 压缩导致质量损失严重）
- **v8.0（当前）**：**检索式提取**（零压缩，信号检索 + 上下文剪裁，6 系列 199 Skill 完成）

---

## 6 阶段蒸馏流水线

### Stage 0: 系列理解（Series Understanding）

| 文件 | 说明 |
|------|------|
| [[methodology/00-overview.md]] | 全景概览（v8.0） |
| [[methodology/01-stage0-series-understand.md]] | 列出剧集、分组主题弧、识别核心论点 |

### Stage 1: ⭐ 检索式提取（Retrieval-based Extraction）

| 文件 | 说明 |
|------|------|
| [[methodology/02-stage1-retrieval-extract.md]] | **核心创新**：保留 29 集完整 VTT 原文（零压缩），7 路提取器以检索信号定位方法论段落 |

### Stage 1.5: 四重验证（Quadruple Verification）

| 文件 | 说明 |
|------|------|
| [[methodology/03-stage1.5-quadruple-verify.md]] | V1 跨域 → V2 预测力 → V3 独特性 → V4 体系兼容 |

### Stage 2: RIA++ 构造

| 文件 | 说明 |
|------|------|
| [[methodology/04-stage2-ria-plus.md]] | R(原文) → I(方法论) → A1(案例) → A2(触发) → E(步骤) → B(边界) |

### Stage 3: 跨系列链接

| 文件 | 说明 |
|------|------|
| [[methodology/05-stage3-cross-series-link.md]] | Zettelkasten 式网状连接 |

### Stage 4: 压力测试

| 文件 | 说明 |
|------|------|
| [[methodology/06-stage4-pressure-test.md]] | 多场景交叉验证 |

### Stage 5: 交付

| 文件 | 说明 |
|------|------|
| [[methodology/07-stage5-deliver.md]] | 部署到 skills 目录 |

---

## 7 路检索式提取器

每个提取器不再"总结"或"概括"，而是**带着检索信号去原文定位**。

| 编号 | 提取器 | 检索信号示例 | 预期产出 |
|------|--------|-------------|----------|
| E1 | [[extractors/01-game-theory-extractor.md\|博弈模型提取器]] | 囚徒困境、胆小鬼、信号博弈、MAD、升级、不对称、近距法则 | 博弈论框架 |
| E2 | [[extractors/02-geopolitics-extractor.md\|地缘法则提取器]] | 心脏地带、修昔底德陷阱、海权、陆权、缓冲区、帝国 | 地缘政治原则 |
| E3 | [[extractors/03-civilization-extractor.md\|文明规律提取器]] | 精英过剩、人口转型、制度僵化、崩溃、Asabiyyah | 文明兴衰规律 |
| E4 | [[extractors/04-religion-extractor.md\|宗教叙事提取器]] | 弥赛亚、千禧年、末世论、一神教、预言 | 宗教/神话结构 |
| E5 | [[extractors/05-predictive-extractor.md\|预测模型提取器]] ⭐ | 如果…那么…、预测、推演、情景、拐点、信号 | 预测推理链 |
| E6 | [[extractors/06-failure-extractor.md\|反例陷阱提取器]] | 错误、误解、陷阱、谬误、偏见、误读 | 思维错误识别 |
| E7 | [[extractors/07-glossary-extractor.md\|术语词典提取器]] | 自创术语、反复出现概念、关键定义 | 核心概念词典 |

---

## 质量保障：四重验证

| 验证 | 核心问题 | 淘汰条件 |
|------|---------|----------|
| V1 跨域 | 至少 2 集有佐证？ | 只在一集出现 → 降级 |
| V2 预测力 | 能推导出未明说的结论？ | 纯描述无推断力 → 淘汰 |
| V3 独特性 | 不是常识？ | 任何人都能想到 → 淘汰 |
| V4 体系兼容 | 与心理史学其他系列不矛盾？ | 与已建立的 Skill 冲突 → 打标 |

**通过率预期**：原始提取池 ~100-200 个候选 → 四重验证后 ~25-50 个（25-50%） → 最终产出 Skill ~15-30 个。

---

## 相关笔记

- [[MOC-心理史学总览]]
- [[MOC-系列目录]]
- [[MOC-Game-Theory]]
- [[SPEC.md]]
- [[PROGRESS.md]]
