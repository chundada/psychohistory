# 🔄 给 AI 代理的接手指南 (Continue for AI Agents)

> 此文件专门为后续 AI 代理（Claude Code、Cursor Agent 等）设计。
> 阅读此文件 + 查看最新 Git 提交 + 浏览仓库文件 = 可继续工作。

---

## 📋 项目概要

**项目**：Psychohistory（心理史学）— 把 @PredictiveHistory YouTube 频道的知识蒸馏为 AI Skill 体系
**仓库**：`github.com/chundada/psychohistory`
**方法论版本**：v11.2 — 检索式提取 + 七层汇聚验证（Convergence Verification）+ 两层规则（必须层/增强层）

---

## 🏗️ 仓库结构

> 目录树单源维护于 `README.md` 的「仓库结构」一节，请以该处为准。

---

## ✅ 已完成：7 个系列 · 209 个 Skill

全部 7 个系列（Origin、Game Theory、Secret History、Geo-Strategy、Interview、Civilization、Great Books）均已蒸馏完成，技能以 RIA/RIA++ 格式单源存储于 `skills/` 目录。各系列集数、技能数、产出明细与最新统计以 `PROGRESS.md` 为唯一口径。

### Game Theory（Pilot）经验总结（对后续系列）

| 学到的教训 | 后续改进 |
|---|---|
| 两阶段摘要提取→信息丢失 | 直接检索式提取（已用） |
| 压力测试不可行（416 测试无人执行） | 跳过，改用 QUICK_START 替代 |
| Zettelkasten Mermaid 图好看无用 | 跳过，INDEX 场景索引更有用 |
| E5 预测模型最丰富（12 个 HIGH） | 后续系列优先投给预测信号 |

---

## ✅ 已完成的工作

> 完整版本记录与每次变更内容见 `PROGRESS.md` 的「方法论版本记录」（当前版本 v11.2），此处不再单独维护。

---

## 📝 工作规范（对 AI 代理）

### Git 提交规范

每次阶段性完成任务后执行：

```bash
git add -A
git commit -m "<emoji> <阶段名>: <做了什么>

- 具体变更条目 1
- 具体变更条目 2
- 当前状态: 下一步该做什么"
git push
```

提交信息用中文，前缀 emoji 规范：
- 🎉 初始/里程碑
- 📥 下载/数据获取
- 🔬 提取/分析
- 🎯 方法论设计/更新
- ✅ 验证/测试
- 📝 文档/模板
- 🔗 链接/体系整合

### 更新 PROGRESS.md

每次提交前更新 PROGRESS.md 中的状态标记：
- `✅` = 完成
- `🔵` = 进行中
- `⏳` = 待处理

### 先读再写

接手工作前，依次阅读：
1. `CONTINUE_FOR_AI.md`（当前文件）— 知道上下文
2. `PROGRESS.md` — 知道进度
3. `SPEC.md` — 知道设计
4. 对应阶段的 `methodology/*.md` — 知道怎么做