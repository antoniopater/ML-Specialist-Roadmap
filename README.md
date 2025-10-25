# ML-Specialist-Roadmap
### My 2–3 year public learning & building plan to become a machine learning / deep learning specialist. Transparent progress, real projects, papers, and MLOps.
---
## TL;DR


### - 📌 Current focus: Machine Learning Specialization - Andrew Ng
### - 🧪 Active project:
### - 🎯 Quarter goal: Finish all moduls from first course
### - 🗓️ This week: I modul in Regression and Classification


---
### Table of Contents
1. Vision & Rules of the game
2. Curriculum & Progress (courses + milestones)
3. Projects (production‑grade)
4. Research Practice (paper log & replications)
5. Skills Matrix (tech & MLOps)
6. Benchmarks & Competitions
7. Public Notes / Writing
8. Roadmap & Changelog
---
### Vision & Rules of the game


Vision: Build end‑to‑end ML systems that solve real problems (healthcare, law, finance).
Rules:
One production project per year + 2–3 small projects.
1 paper/week: read → reproduce a key ablation → short note.
Publicly track progress (this README), keep code clean, measure value.
Domains I’m exploring:
🩺 Healthcare (tabular/CV) — triage from blood panels, segmentation.
⚖️ Legal NLP / RAG — retrieval, reranking, faithfulness metrics.
📈 RL in Trading — risk‑aware baselines, transaction costs, walk‑forward.


---
## Curriculum & Progress
Progress legend: ✅ done • 🔄 in progress • ⏳ planned
### Foundations (0–6 months)
⏳ fast.ai – Practical Deep Learning for Coders


Repo notes: `01_course_notes/fastai/`


🔄 DeepLearning.AI – Machine Learning Specialization (Ng)


Repo notes: `01_course_notes/ng-ml-spec/`


⏳ DeepLearning.AI – Deep Learning Specialization (Ng)


Repo notes: `01_course_notes/ng-dl-spec/`


### Specializations (6–18 months)
⏳ Stanford CS231n (CV) — convnets, modern architectures


Notes: `01_course_notes/cs231n/`


⏳ Stanford CS224n (NLP) — transformers, attention, seq2seq


Notes: `01_course_notes/cs224n/`


⏳ Hugging Face – LLM Course — transformers/datasets/accelerate


Notes: `01_course_notes/hf-llm/`


### MLOps / Production (12–24 months)
⏳ Full Stack Deep Learning — data → train → deploy → monitor


Notes: 01_course_notes/fsdl/


⏳ ML in Production (DLAI) — pipelines, registries, CI/CD


Notes: 01_course_notes/dlai-ml-prod/


### Math & Stats (anytime)

⏳ Linear Algebra refresh (SVD, eigens, norms)


⏳ Prob/Stats (Bayes, calibration, uncertainty)


⏳ Optimization (GD/Adam, LR schedules, regularization)


---
## Projects (production‑grade)


---
## Research Practice (Paper Log)


1 paper/week → small reproduction or ablation. Keep it honest and brief.
Log format (`02_papers/`):
`YYYY‑MM‑DD  |  Paper Title  |  Link  |  What I reproduced  |  Key takeaway  |  Next experiment`
Examples:
`2025‑10‑12 | Attention Is All You Need | link | Re‑ran small Transformer on toy task | Scaling laws intuition | Try RoPE/ALiBi`
`2025‑10‑05 | BERT | link | MLM fine‑tune on domain corpus | Tokenization matters | Add reranker baseline`


---
## Benchmarks & Competitions


---
## Public Notes / Writing


---
## Roadmap & Changelog


---

### Repository Structure
```Bash
ML-Specialist-Roadmap/
├─ 01_course_notes/
│ ├─ fastai/
│ ├─ ng-ml-spec/
│ ├─ ng-dl-spec/
│ ├─ cs231n/
│ ├─ cs224n/
│ └─ hf-llm/
├─ 02_papers/
│ └─ paper-log.md
├─ 03_projects/
│ ├─ prokect-01/
├─ 04_templates/
│ └─ project_template/
├─ benchmarks/
├─ notes/
├─ talks/
├─ .github/workflows/ci.yml
├─ pyproject.toml
├─ requirements.txt or uv.lock
├─ Makefile
└─ README.md (this file)
```

