---
tags: [psychohistory, methodology]
stage: "Stage 5"
status: "deprecated"
---
# Stage 5：交付（Delivery）

> **⚠️ 已归档废弃**：独立交付阶段已取消，交付并入常规流程（现行 3 步流水线不含此阶段）。本文件仅作历史存档，请勿遵循。

> **目标**：将已验证的技能以标准格式交付，并生成精华阅读文档
> **输入**：`skills/` 目录中通过压力测试的 SKILL.md 文件 + `INDEX.md`
> **输出**：`DIGEST.md`（5000-10000 字）+ 安装到系统技能目录

---

## 一、交付物概览

| 交付物 | 目的 | 字数 | 受众 |
|--------|------|------|------|
| SKILL.md（每个技能） | 完整技能文档 | 500-1500 字/篇 | 需要深度使用的分析者 |
| DIGEST.md | 精华阅读，快速掌握核心 | 5000-10000 字 | 需要了解系列精华的人 |
| 系统安装 | 集成到 AI 助手/IDE | - | 日常使用者 |

---

## 二、DIGEST.md 生成指南

### 2.1 结构要求

```markdown
# <系列名称>：知识蒸馏精华阅读

> 基于 RIA-TV++ 管道从 <集数> 集视频中提取的 <技能数> 个可复用认知技能。

## 一、系列简介

（300-500 字）来自 SERIES_OVERVIEW.md 的核心 thesis 和结构。

## 二、核心框架

（1000-2000 字）对整个系列最核心的 3-5 个技能进行简介。
每个技能以"一句话 + 核心洞察 + 触发时机"的格式呈现。

## 三、技能精要

（2000-4000 字）每个技能的 R 和 I 部分的关键内容。
按主题分组，每组 3-5 个技能。

### 3.1 主题组 1

#### 技能 1：<名称>
- **核心洞察**：一句话
- **原话引用**：R 中最精炼的一句话
- **方法论**：I 的精简版
- **触发时机**：A2 的一句话版本
- **链接**：→ related_skills

#### 技能 2：<名称>
...

### 3.2 主题组 2
...

## 四、技能组合推荐

（500-1000 字）来自 INDEX.md 的使用指南部分。
每个场景给出 2-3 条推荐路径。

## 五、应用边界

（300-500 字）来自 SERIES_OVERVIEW.md 的关键局限性。
明确什么情况下不应该使用这些技能。

## 六、快速导航

（200-300 字）指向完整的 SKILL.md 文件和 INDEX.md。
```

### 2.2 生成方法

DIGEST.md 不是手写的，而是从现有文档自动合成：

```
DIGEST.md 来源：
├── 系列简介 ← SERIES_OVERVIEW.md 的 core_thesis + interpretive_framework
├── 核心框架 ← 各个 SKILL.md 的 I 字段精华
├── 技能精要 ← 各个 SKILL.md 的 R + I 字段精简版
├── 技能组合 ← INDEX.md 的使用指南
├── 应用边界 ← SERIES_OVERVIEW.md 的 critical_limitations
└── 快速导航 ← 自动生成的链接列表
```

### 2.3 字数控制

DIGEST.md 的目标是让读者在 **15-20 分钟内**掌握该系列的精华。

- 5000 字：技能少（3-5 个）的系列
- 7000 字：中等规模系列
- 10000 字：大型系列（6-10 个技能）

---

## 三、系统安装

### 3.1 Claude 技能目录

```bash
# 创建技能目录
mkdir -p ~/.claude/skills/Psychohistory/

# 复制所有文件
cp -r skills/*.md ~/.claude/skills/Psychohistory/
cp INDEX.md ~/.claude/skills/Psychohistory/

# 可选：生成自动加载配置
echo "
# Psychohistory skills
# 加载方式见 ~/.claude/skills/Psychohistory/INDEX.md
" >> ~/.claude/skills/config.yml
```

### 3.2 Cursor IDE 技能目录

```bash
# 创建技能目录
mkdir -p .cursor/skills/Psychohistory/

# 复制所有文件
cp -r skills/*.md .cursor/skills/Psychohistory/
cp INDEX.md .cursor/skills/Psychohistory/
```

### 3.3 安装检查清单

- [ ] 所有 SKILL.md 已复制到目标目录
- [ ] INDEX.md 已复制到目标目录
- [ ] 权限设置正确
- [ ] AI 助手可以正确读取技能文件（对话测试）

---

## 四、交付后维护

### 4.1 版本管理

所有交付物应在 Git 仓库中管理：

```bash
cd Psychohistory/
git init
git add .
git commit -m "feat: 初始交付 <系列名称> v1.0"
```

### 4.2 版本号规范

| 版本 | 含义 | 触发条件 |
|------|------|---------|
| v1.0 | 初始交付 | 首次完成所有 Stage |
| v1.x | 小修 | 修正拼写、格式、链接 |
| v2.0 | 大修 | 添加新技能、重构 INDEX.md |
| v2.x | 增量更新 | 基于同一系列的新剧集补充 |

### 4.3 更新日志

每次更新时维护 `CHANGELOG.md`：

```markdown
# 变更日志

## v1.0 - YYYY-MM-DD
### 新增
- 初始交付 <系列名称>
- 共 N 个技能，覆盖 M 个主题组
```

---

## 五、质量门禁 QG7（最终检查）

在标记为"完成"之前，检查：

- [ ] DIGEST.md 字数在 5000-10000 之间
- [ ] DIGEST.md 包含所有 6 个部分
- [ ] 所有 SKILL.md 已通过 Stage 4 压力测试（>= 80%）
- [ ] INDEX.md 已更新并包含最新技能
- [ ] 所有文件已复制到目标技能目录
- [ ] Git 仓库已初始化并提交

---

## 六、常见的交付后问题

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 技能在对话中从未被触发 | A2 不够具体或场景覆盖率低 | 回到 Stage 2 强化 A2 |
| DIGEST 太长没人读 | 超过 10000 字 | 精简到 7000 字以内 |
| 与其他技能系统冲突 | Stage 1.5 V4 检查不充分 | 重新运行 V4，更新 INDEX.md |
| 技能内容随时间过时 | 系列涉及时效性信息 | 定期检查并更新 |
