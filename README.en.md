# Psychohistory — A Knowledge Distillation Framework for Predictive Historical Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills: 209](https://img.shields.io/badge/Skills-209-brightgreen)]()
[![Series: 7](https://img.shields.io/badge/Series-7-blue)]()
[![Status: Active](https://img.shields.io/badge/Status-Active-ff6600)]()

---

## Overview

Psychohistory distills analytical frameworks spanning game theory, geopolitics, civilization cycles, and religious narrative analysis into **209 structured, reusable Skill files** that any AI can invoke.

The core premise: historical prediction is not fortune-telling. It is a **multi-framework cross-validation method** based on identifiable structural patterns, boundary conditions, and falsifiable logical chains.

> **Methodology v9.1** · Core method: **Seven-Layer Convergence Verification** — cross-references 7+1 independent analytical frameworks to boost confidence via convergence scoring. See `methodology/08-stage6-convergence-verify.md`.

---

## What This Project Produces

| Deliverable | Description |
|---|---|
| **209 Skill files** | Structured analysis frameworks in RIA/RIA++ format, each containing reading, interpretation, application, and boundary conditions |
| **PSYCHOHISTORY_SYSTEM_PROMPT.md** | Complete persona activation prompt — paste into any AI to instantiate the analyst role |
| **QUICK_START.md** | Scenario-to-skill lookup table (22 scenarios mapped to recommended skill combinations) |
| **INDEX.md** | Zettelkasten-style skill index with trigger scenarios |
| **DIGEST.md** | Curated long-read summary of the Game Theory series |

---

## Methodology: Retrieval-Based Distillation

Traditional knowledge distillation follows a "compress → summarize" pipeline that suffers from irreversible information loss. This project uses a **retrieval-based extraction** approach:

1. **Zero-compression source retention**: Raw lecture transcripts are preserved in full
2. **7 parallel extractors**: Each extractor targets a specific analytical domain with tailored retrieval signals
3. **Direct extraction from full context**: Methodologies are clipped from complete transcripts with source timestamps, enabling traceable verification
4. **Quadruple validation**: Each candidate passes through four independent filters before acceptance

### Extractor Architecture

| Extractor | Retrieval Signals | Output Type |
|---|---|---|
| **Game Model** | prisoner dilemma, asymmetry, escalation, MAD | Game theory frameworks |
| **Geopolitical** | heartland, Thucydides trap, chokepoint | Geopolitical laws |
| **Civilization** | elite overproduction, asabiyyah, collapse | Civilization cycle models |
| **Religious Narrative** | messianic, eschatology, monotheism | Narrative decoding |
| **Predictive Model** | if...then, predict, scenario, tipping point | Prediction logic chains |
| **Economic/Financial** | debt, bubble, inflation, dollar, credit crisis | Economic frameworks |
| **Glossary** | defined as, by this I mean, coined | Core definitions |

---

## Current Status

**7 series completed · 209 Skill files · ~90% of total lecture content processed**

| Series | Episodes | Skills | Format | Location |
|---|---|---|---|---|
| Psychohistory Origin | — | 6 | RIA (R/I/A/B) | `skills/ph-origin-*.md` |
| Game Theory | 29 | 52 | RIA++ (R/I/A1/A2/E/B) | `skills/gt-*.md` |
| Secret History | 28 | 46 | RIA (R/I/A/B) | `skills/sh-*.md` |
| Geo-Strategy | 19 | 35 | RIA (R/I/A/B) | `skills/gs-*.md` |
| Interview (Jang Let's Talk) | — | 10 | RIA | `skills/interview-*.md` |
| Civilization | 62 | 50 | RIA (R/I/A/B) | `skills/civ-*.md` |
| Great Books | 13 | 10 | RIA (R/I/A/B) | `skills/gb-*.md` |

---

## Analytical Capabilities

The skill library covers seven domains:

| Domain | Core Frameworks |
|---|---|
| **Game Theory** | Asymmetry principle, escalation calibration, proximity law, immigration trap, elite overproduction dynamics |
| **Geopolitics** | Three laws of geopolitics, chokepoint control, currency war dynamics, dollar addiction model |
| **Civilization Cycles** | Asabiyyah, EOC model, institutional sclerosis, fertility leading indicators, mercenary overthrow |
| **Religious Narrative** | Eschatological convergence, messianic accelerationism, kabbalistic redemption, AI as religion |
| **Predictive Models** | Multi-framework convergence, empire decline triad, civil war projection, causal chain analysis |
| **Failure Modes** | Great man fallacy, AI consciousness illusion, correlation-causation fallacy, false dichotomy |
| **Terminology** | Mosaic defense, elite overproduction, reality hallucination, technate |

Each skill follows a consistent structure: **source reading → interpretation as methodology → author's application → trigger conditions → execution steps → boundary conditions**, enabling systematic cross-validation.

---

## Quick Start

### Option A: Clone and Install

```powershell
git clone https://github.com/chundada/psychohistory.git
cd psychohistory
PowerShell -ExecutionPolicy Bypass .\_install_skills.ps1
```

### Option B: Use with Any AI

Copy `PSYCHOHISTORY_SYSTEM_PROMPT.md` as the system prompt. The AI will automatically:

1. Activate the psychohistorian persona
2. Select 2-4 relevant skills from the library
3. Apply **multi-framework convergence validation**
4. Self-calibrate using the failure mode checklist
5. Output **conditional predictions** with explicit boundary conditions

---

## Repository Structure

```
Psychohistory/
├── PSYCHOHISTORY_SYSTEM_PROMPT.md   ⬅ Persona activation prompt
├── skills/                            ⬅ 209 structured Skill files
│   ├── ph-origin-*.md                 Psychohistory Origin (6)
│   ├── gt-*.md                        Game Theory (52)
│   ├── sh-*.md                        Secret History (46)
│   ├── gs-*.md                        Geo-Strategy (35)
│   ├── interview-*.md                 Interview (10)
│   ├── civ-*.md                       Civilization (50)
│   └── gb-*.md                        Great Books (10)
├── cases/                             ⬅ Case studies (multi-framework demonstrations)
├── QUICK_START.md                     ⬅ Scenario-to-skill lookup
├── DIGEST.md                          ⬅ Curated reading
├── INDEX.md                           ⬅ Zettelkasten trigger index
├── PROGRESS.md                        ⬅ Project progress tracking
├── CLAUDE.md                          ⬅ AI workspace configuration
├── extractors/                        ⬅ 7 retrieval-based extractors
├── methodology/                       ⬅ Distillation pipeline SOPs
├── series/                            ⬅ Source transcripts by series
│   ├── psychohistory-origin/
│   ├── game-theory/
│   ├── geo-strategy/
│   ├── secret-history/
│   ├── interview-jang-letstalk/
│   ├── civilization/
│   └── great-books/
└── SPEC.md                            ⬅ Design specification
```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  209 psychohistorical models · 7 series · actively expanding<br/>
  <em>"The purpose of prediction is not to foresee the future — but to make it better."</em>
</p>
