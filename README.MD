# Applied Data Science

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

## Overview
This repository contains hands-on implementations, exercises, and mini-projects completed while learning **Data Science and Data Engineering**. It follows a structured learning approach:

- Each **course** has multiple **modules**
- Each **module** contains code, examples, exercises, and small tasks
- Each **final-project** applies the concepts learned in the course

The goal is to demonstrate both **theoretical understanding** and **practical application** of the concepts.

---

## Repository Structure
```text
applied-data-science/
│
├── courses/
│   ├── sql-data-engineering/
│   │   ├── module-01-basics/
│   │   ├── module-02-joins/
│   │   ├── module-03-window-functions/
│   │   └── final-project/
│   │
│   ├── python-for-data/
│   │   ├── module-01-basics/
│   │   ├── module-02-pandas/
│   │   ├── module-03-data-cleaning/
│   │   └── final-project/
│   │
│   └── machine-learning/
│       ├── module-01-supervised/
│       ├── module-02-unsupervised/
│       └── final-project/
│
├── mini-projects/   # Independent projects applying multiple courses
├── datasets/        # Sample datasets used in exercises/projects
└── README.md        # This file
` ` `  ← remove spaces, this is just to avoid closing the outer code block

---
...rest of file unchanged
```

**What was fixed:**

1. **Missing code fence around the directory tree** — without ` ```text ``` `, the `│`, `├──`, and `└──` characters don't render properly as a tree; they just appear as jumbled text.
2. **Indentation inside `machine-learning/`** — its sub-modules were at the wrong nesting level (aligned with the course folders instead of being indented as children). Fixed so they're properly nested under `machine-learning/` with consistent spacing to match the other courses.