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
3. Books – Python (Effektywny Python)
4. Projects (production‑grade)
5. Research Practice (paper log & replications)
6. Skills Matrix (tech & MLOps)
7. Benchmarks & Competitions
8. Public Notes / Writing
9. Roadmap & Changelog

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

✅ DeepLearning.AI – Machine Learning Specialization (Ng)
certification: https://www.coursera.org/account/accomplishments/certificate/UBI1V10CXDRN

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

## Books – Python (Effektywny Python)

Czytam **Effektywny Python** (Effective Python, 3rd ed.) i równolegle podciągam Pythona: robię notatki z rozdziałów oraz notebooki z kodem z książki, żeby utrwalać idiomy i dobre praktyki.

- Notatki: `01_course_notes/effective-python/` — streszczenia rozdziałów, wnioski.
- Notebooki: `notebooks/effective-python/` — kod z rozdziałów, własne eksperymenty, ćwiczenia.

Progress: ⏳ planned (rozpoczęcie po ustaleniu)

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
├─ 01_course_notes/          # Course notes and summaries
│  ├─ fastai/                # fast.ai course notes
│  ├─ ng-ml-spec/            # Machine Learning Specialization (Ng) ✅
│  ├─ ng-dl-spec/            # Deep Learning Specialization (Ng)
│  ├─ cs231n/                # Stanford CS231n (Computer Vision)
│  ├─ cs224n/                # Stanford CS224n (NLP)
│  ├─ hf-llm/                # Hugging Face LLM Course
│  ├─ fsdl/                  # Full Stack Deep Learning
│  ├─ dlai-ml-prod/          # ML in Production (DLAI)
│  └─ effective-python/     # Effektywny Python – notatki z rozdziałów
├─ notebooks/                # Jupyter notebooks with code implementations
│  ├─ fastai/                # fast.ai course notebooks
│  ├─ ng-ml-spec/            # Machine Learning Specialization (Ng) ✅
│  │  ├─ 2025_10_19_Supervised_Machine_Learning_Regression_and_Classification.ipynb
│  │  ├─ 2025_11_08_Linear_Regression.ipynb
│  │  └─ 2025_11_16_Logistic_Regression.ipynb
│  ├─ ng-dl-spec/            # Deep Learning Specialization (Ng)
│  ├─ cs231n/                # Stanford CS231n (Computer Vision)
│  ├─ cs224n/                # Stanford CS224n (NLP)
│  ├─ hf-llm/                # Hugging Face LLM Course
│  ├─ fsdl/                  # Full Stack Deep Learning
│  ├─ dlai-ml-prod/          # ML in Production (DLAI)
│  └─ effective-python/      # Effektywny Python – notebooki z rozdziałów
├─ 02_papers/                # Paper reading log and reproductions
│  └─ paper-log.md           # Weekly paper log
├─ 03_projects/              # Production-grade ML projects
├─ 04_templates/             # Project templates
│  └─ project_template/      # Template for new projects
├─ benchmarks/               # Benchmark results and comparisons
├─ notes/                    # General notes and thoughts
├─ talks/                    # Conference talks and presentations
├─ scripts/                  # Utility scripts for repository maintenance
├─ .github/
│  └─ workflows/             # CI/CD workflows
├─ .gitignore                # Git ignore rules
├─ pyproject.toml            # Python project configuration
├─ requirements.txt          # Python dependencies
├─ Makefile                  # Common commands
├─ LICENSE                   # MIT License
└─ README.md                 # This file
```

### Naming Convention

- **Files**: Use underscores instead of spaces (e.g., `2025_11_16_Logistic_Regression.md`)
- **Format**: `YYYY_MM_DD_Topic_Name.ext`
- **Directories**: Use lowercase with hyphens (e.g., `ng-ml-spec`)
