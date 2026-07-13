---
tags: [psychohistory, extractor]
extractor_type: "finance-economy"
status: "active"
---

# E6 经济金融模式提取器 (Finance & Economy Extractor)

> **v4.2 新增**：取代原来的反例陷阱提取器。
>
> 经济/金融内容是 @PredictiveHistory 的核心分析维度之一——从美元霸权机制到债务危机链，从资产泡沫到制裁经济学。Game Theory 的 GT06(世界银行)、GT17(大重置)、GT27(普京经济战)；Geo-Strategy 的 GS04(沙特)、GS03(帝国如何摧毁美国)、GU08(西方为何完蛋) 以及 Interview(日元套利交易) 中都有密集的经济金融分析。关键词在全库中命中 **>4000 次**，是真正的富矿区。
>
> **反例陷阱不再是独立提取器**：失败模式防护改为在 RIA+ 构造时内嵌检查（写 B 段时自然完成）。

---

## 用途 (Purpose)

从视频转录文本中提取**经济与金融分析框架**相关的知识条目。识别主讲人关于宏观经济趋势、金融系统结构、货币机制、债务动力学、制裁与贸易战的经济逻辑等方面的框架性分析。每个提取条目都应当是可复用的经济推理工具。

---

## 范围 (Scope)

### 属于此提取器的内容

#### 1. 美元霸权与货币体系 (Dollar Hegemony & Monetary System)
- 美元作为储备货币的机制与代价
- 石油美元体系（Petrodollar）的运作与挑战
- 去美元化（De-dollarization）的趋势与限制
- 货币战争：汇率操纵、资本管制、货币互换协议
- 国际货币体系改革（特别提款权、数字货币、BRICS 货币）
- 美联储政策对全球的溢出效应

#### 2. 债务与危机动力学 (Debt & Crisis Dynamics)
- 主权债务危机：触发条件、传染路径、违约后果
- 私人信贷泡沫（Private Credit Bubble）：形成→膨胀→破裂循环
- 公司债/垃圾债市场的风险信号
- 系统性金融风险的识别指标
- 银行挤兑、影子银行、流动性危机
- 债务上限博弈与政府关门

#### 3. 资产泡沫识别 (Asset Bubble Identification)
- 资产泡沫的典型生命周期：替代→繁荣→非理性→崩溃
- 不同资产类别泡沫的共性特征（股票、房地产、加密货币、AI投资）
- 泡沫爆破的触发事件与时序
- 泡沫后的经济后果：通缩螺旋 vs 滞胀

#### 4. 制裁经济学 (Sanctions Economics)
- 金融制裁的机制（SWIFT、冻结资产、禁止交易）
- 制裁的有效性条件与反作用
- 被制裁国的适应策略：平行支付系统、易货贸易、加密货币
- 制裁作为"双刃剑"：对制裁国自身的成本
- 次级制裁的威慑力与边界

#### 5. 供应链与全球化断裂 (Supply Chain & Globalization Fracture)
- 供应链重构（Near-shoring, Friend-shoring, China+1）
- 能源安全与价格冲击
- 关键矿产与资源地缘政治
- 粮食危机与化肥/航运成本
- 贸易战与关税的经济传导机制

#### 6. 通胀/通缩/滞胀分析 (Inflation/Deflation/Stagflation)
- 通胀驱动因素的拆解（需求拉动 vs 成本推动 vs 货币超发）
- 通胀预期的锚定与失锚
- 通缩螺旋的触发条件
- 滞胀的成因与历史先例（1970s）
- 日本化（Japanification）：长期低增长+低利率+高债务

#### 7. 央行与货币政策 (Central Banking & Monetary Policy)
- 量化宽松（QE）与量化紧缩（QT）的传导机制
- 利率政策的限制：零利率下限、反转利率
- 央行独立性的政治挑战
- 现代货币理论（MMT）的实践与争议
- 日元套利交易（Yen Carry Trade）的全球影响

### 不属于此提取器的内容
- 基础经济学教科书内容（供需曲线、GDP定义等）
- 不涉及分析框架的单一金融数据点（如"某日股市涨了X%"）
- 纯公司金融/企业财务细节
- 不涉及体系分析的个人投资建议

---

## 检索信号 (Search Signals)

### 关键词与短语
```
debt crisis·debt ceiling·sovereign debt·default·bankruptcy·credit crunch
credit bubble·credit default swap·liquidity·solvency·leverage·margin call
inflation·deflation·hyperinflation·stagflation·CPI·consumer price
dollar hegemony·petrodollar·de-dollarization·reserve currency·exorbitant privilege
sanctions·financial sanctions·SWIFT·asset freeze·secondary sanctions
central bank·Federal Reserve·interest rate·rate hike·rate cut
quantitative easing·QE·quantitative tightening·QT·tightening·loosening
yen carry trade·carry trade·arbitrage·capital flight·hot money
bubble·speculative·overvaluation·irrational exuberance·Minsky moment
collapse·crash·meltdown·bank run·financial crisis·systemic risk
supply chain·bottleneck·logistics·shipping·commodity·oil price·energy crisis
trade war·tariff·trade deficit·protectionism
recession·depression·slowdown·stagflation·japanification
currency war·exchange rate·devaluation·competitive devaluation
GCC·OPEC·petrodollar·oil weapon·energy transition
```

### 结构性信号
- 数字量化分析（"X万亿美元"、"X%的GDP"、"Y年周期"）
- 因果关系链条（"A导致B→B导致C→C导致经济危机"）
- 对比陈述（"这不像2008年，因为…"）
- 时间戳预测（"X年后我们将看到…"、"在Y年之前…"）
- 警示性陈述（"真正危险的是…"、"没人注意到的是…"）
- 历史类比（"这像1930年代的大萧条"、"像1970年代的滞胀"）

---

## 提取检查清单

- [ ] 是否是从视频中提取的**方法论框架**而非单纯的事实陈述？
- [ ] 是否包含主讲人的**分析逻辑**（因果关系、条件关系、对比关系）？
- [ ] 是否可以作为独立的经济分析工具使用？
- [ ] 是否标注了 `[source]` = 文件名 + 时间戳范围？
- [ ] 是否附带了中文解读（2-4句）？
