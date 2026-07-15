---
name: "因果链预测模型"
description: "通过'如果A则B'的双节点因果链推演，从单一异常事件推导出完整冲突时间线的预测方法"
source_series: "Interview"
source_episodes:
  - "Let's Talk w/ Cyrus Jansen"
tags:
  - psychohistory
  - interview
  - predictive-model
created: 2026-07-13
updated: 2026-07-13
---

# 因果链预测模型

> **来源**：Interview · @PredictiveHistory
> **一句话**：将两个看似独立的事件通过"如果 A 则 B"的因果链链接起来——每一步推理都必须逻辑自洽，且每一步的置信度可被独立评估。

---

## R — Reading（阅读原文）

> [Interview]
> "But you could surmise that if he were to come back into office, then he would declare war on Iran, right? So, these two things were linked together. If Donald Trump could win in 2024, then he would most certainly declare war against Iran. So, we're now entering into the, you know, fifth month of this conflict."

> "these two things were linked together"

---

## I — Interpretation（方法论解读）

Jang 预测方法的第二个层次是"因果链"（causation chain）——将异常检测的结果转化为一个"如果 A 则 B"的可检验预测。这是一个双节点逻辑模型：(1) 异常信号 S（索莱马尼刺杀）→ 意图 I（特朗普欲对伊开战）；(2) 条件事件 A（特朗普 2024 年胜选）→ 结果事件 B（对伊战争爆发）。关键方法论特征：第一，每一步因果链都是独立的可证伪命题；第二，Jang 使用"most certainly"而非"100% certain"——这是概率化表达而非绝对断言；第三，链中可嵌入延迟变量（"因为 2020 年败选，战争被推迟"），使模型能适应时间维度的变化。

---

## A — Application（应用与执行）

**触发条件**：当已经识别出一个异常信号并初步推断出隐藏意图后，需要将意图转化为对未来事件的时序预测时使用。

**作者案例**：Jang 教授用这个模型构建了从"索莱马尼刺杀"到"2024 年特朗普胜选"再到"对伊战争爆发"的完整预测链条，这一链条在 2025 年得到验证。

**执行步骤**：
1. **锚定起始节点**：以异常事件的识别结果作为因果链的起点（A0 = 异常信号）。
2. **推导隐藏意图**：从 A0 推导出行为体的隐藏意图（I1 = "特朗普想对伊开战"）。
3. **确定触发条件**：识别使意图转化为行动的必要外部条件（C1 = "特朗普 2024 年胜选"）。
4. **链接结果**：将触发条件与可观察的结果链接（R1 = "对伊战争在 2025 年爆发"）。
5. **引入延迟/干扰变量**：考虑可能中断因果链的事件（如 2020 年败选作为"延迟器"）。
6. **概率标注**：为每个节点标注置信度——"most certainly" ≈ >80% 置信度，"possibly" ≈ 30-60%。

---

## B — Boundary（边界条件）

- 当因果链超过三个节点时，预测可靠性呈指数下降（误差级联效应）。
- 不适用于存在复杂多变量反馈回路的高度动态系统（如股市预测或加密货币价格）。
- 当触发条件本身高度不确定时（如"如果某位领导人意外死亡"），因果链预测退化为一厢情愿的想象。
- 无法处理"黑天鹅"事件——因果链建立在已知变量基础上，无法预测完全不可知的外部冲击。
