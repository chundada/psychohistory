# Obsidian 配置优化

## 需要安装的社区插件

先打开 Obsidian → 设置 → 社区插件 → 浏览，搜索安装：

### 必装（3 个）

| 插件 | 为什么需要 |
|---|---|
| **Dataview** | 把 SKILL.md 的 YAML frontmatter 变成可查询的表格 |
| **Graph Analysis** (已自带) | 用图谱看 Skill 之间的链接关系 |
| **Tag Wrangler** | 管理标签（psychohistory·predictive-model·game-theory 等） |

### 强烈推荐（4 个）

| 插件 | 为什么需要 |
|---|---|
| **Kanban** | 把待处理的系列和 Stage 做成看板 |
| **Excalidraw** | 画 Skill 之间的组合流程图 |
| **Obsidian Charts** | 把 Skills 统计做成可视化图表 |
| **Better Word Count** | 写作时看进度 |

## Obsidian 在这个项目里的最佳用法

### 1. 日常学习：用图谱浏览知识网络

打开 Obsidian 图谱（左侧菜单）：

- **所有节点** = 117 个 SKILL.md + 方法论文档 + 提取器
- **没有链接的节点** = 我还没写内部 `[[wikilinks]]`（项目偏工具性而非网络性）
- **建议**：阅读时随手加 `[[相关Skill]]`，图谱会越来越丰富

### 2. 快速检索：用标签过滤

每个 SKILL.md 都有 YAML frontmatter，支持标签搜索：

```
# 查找所有预测模型
搜索栏输入：tag:#predictive-model
# 查找博弈论相关内容
搜索栏输入：tag:#game-theory
# 查找 Secret History 的宗教分析
搜索栏输入：tag:#secret-history tag:#religion-narrative
```

### 3. Dataview 查询（安装后）

打开任意笔记，粘贴以下代码看实时表格：

```dataview
TABLE description as "描述", v2_prediction_strength as "预测力"
FROM "skills"
WHERE v2_prediction_strength = "strong"
SORT file.name ASC
```

```dataview
TABLE rows.file.link as "Skills"
FROM "skills"
GROUP BY tags
SORT rows.file.name ASC
```

### 4. 学习路径：按顺序通读

**第一周 — 建立全景**
```markdown
1. 打开 DIGEST.md → 10 分钟读完精华
2. 打开 QUICK_START.md → 知道什么场景用什么 Skill
3. 通读 5 个核心 skill：
   - [[gt-predictive-003]]  多重框架汇聚验证法 ⭐
   - [[gt-game-theory-asymmetry]]  非对称法则
   - [[gt-geopolitics-three-laws]]  地缘政治三定律
   - [[gt-civilization-eoc-model]]  三维社会动力模型
   - [[gt-religion-eschatology-geopolitics]]  末世论作为地缘政治编码
```

**第二周 — 深入学习**
```markdown
- 预测模型组（12 个）：从 [[gt-predictive-003]] 开始逐一阅读
- 博弈论组（8 个）：non-proximity → escalation → asymmetry
- 地缘组（6 个）：chokepoint → currency war → three laws
```

**第三周 — Secret History 哲学层次**
```markdown
- [[sh-civ-001]] 文明生命周期
- [[sh-civ-013]] 天命
- [[sh-rel-010]] 耶稣的神性火花
- [[sh-rel-019]] 犹太和平
- [[sh-civ-008]] 罗马反文明
```

### 5. 记笔记的方法

在 Obsidian 中新建笔记，用 `[[wikilinks]]` 关联 Skill：

```markdown
---
tags: [psychohistory, my-notes]
created: 2026-07-13
---

# 我对中美关系的分析

今天看了新闻，感觉可以用 [[gt-geopolitics-three-laws]] 来分析。

根据地缘政治三定律，美国（强者）和俄罗斯（强者）在互相尊重...
而中国作为崛起者...

进一步用 [[gt-predictive-003]] 多重框架汇聚验证：
- 地缘框架 → 咽喉要道冲突
- 经济框架 → 货币战争
- 文明框架 → 精英过剩

→ 三个框架汇聚于"冲突将继续"→ 高可信度
```

这样你写的笔记会自动出现在 Obsidian 图谱中，和 Skill 形成知识网络。

### 6. 我的建议布局

**左侧面板**（固定）：
- 文件浏览器 → 按目录看
- 标签面板 → 按标签过滤

**右侧面板**：
- 大纲 → 看当前笔记的结构
- 反向链接 → 看当前 Skill 被哪些笔记引用

**主面板**：阅读/编辑

### 7. 更新 `打开库.ps1`

现有的 `_打开库.ps1` 已经 OK。你也可以手动：
```
Obsidian → 打开另一库 → 选择 Psychohistory 文件夹
```
