# Data Lifecycle

## Data Processing Hierarchy

```
DATA PROCESSING (the entire umbrella)
│
│   The whole journey of data from collection to final use
│
│
├── DATA COLLECTION
│       │
│       └── Acquiring raw data only — zero transformation
│               ├── Web scraping
│               ├── API calls
│               ├── Surveys / Forms
│               ├── Sensors / IoT
│               ├── Database queries
│               └── Downloading datasets
│
│
├── DATA PREPARATION
│       │
│       └── Clean / Transform / Wrangle → for BI / Analytics
│               │
│               ├── DATA WRANGLING TECHNIQUES (shared with preprocessing)
│               │       ├── Joining / Merging tables
│               │       ├── Pivoting (wide ↔ long)
│               │       ├── Splitting columns
│               │       ├── Flattening nested data (JSON/XML)
│               │       ├── Aggregating records
│               │       ├── Filtering / Subsetting
│               │       └── Reordering / Renaming columns
│               │
│               └── DESTINATION
│                       ├── Descriptive Analysis (what happened?)
│                       └── Diagnostic Analysis  (why did it happen?)
│
│
└── DATA PREPROCESSING
        │
        └── Clean / Transform / Wrangle → for ML Models
                │
                │   DATA WRANGLING TECHNIQUES (same as preparation)
                │
                │
                ├── INITIAL TRAINING (first time ever)
                │       ├── Build cleaning/transforming/wrangling rules
                │       ├── Train the model on prepared data
                │       ├── Test / Evaluate on unseen data
                │       ├── ❌ Not accurate → try new/modified rules
                │       │       └── loop back until accurate
                │       └── ✅ Accurate → lock in rules → DEPLOY
                │
                │
                ├── INFERENCE PREPROCESSING (after deployment)
                │       │
                │       └── Recurring — every real world prediction
                │               ├── Apply EXACT locked-in rules from training
                │               ├── Feed cleaned data into deployed model
                │               ├── Model returns prediction
                │               └── Monitor accuracy over time
                │                       ↓
                │                       ↓ accuracy drops detected
                │                       ↓
                │               ┌───────────────────────┐
                │               │  HOW MUCH DID IT DROP? │
                │               └───────────────────────┘
                │                       │
                │                       ├── 🟢 SMALL
                │                       ├── 🟡 MODERATE
                │                       └── 🔴 SIGNIFICANT
                │
                │
                ├── 🟢 CONTINUOUS LEARNING (small drop)
                │       ├── Keep all existing rules
                │       ├── Add new rules on top
                │       ├── AND/OR feed new real-world data
                │       ├── Re-evaluate → highest accuracy?
                │       └── ✅ Deploy → resume inference preprocessing
                │
                │
                ├── 🟡 PARTIAL RETRAINING (moderate drop)
                │       ├── Try Option A:
                │       │       └── Add new rules to existing logic
                │       ├── Try Option B:
                │       │       └── Build completely new logic
                │       ├── Compare A vs B → which is most accurate?
                │       └── ✅ Deploy winner → resume inference preprocessing
                │
                │
                └── 🔴 FULL MODEL RETRAINING (significant drop)
                        ├── Scrap ALL existing rules entirely
                        ├── Build brand new cleaning/transforming/wrangling logic
                        ├── Train → Test → Evaluate from scratch
                        └── ✅ Deploy → resume inference preprocessing
```

## Triggers That Activate Retraining

```
│
├── Data Drift        → incoming data looks different from training data
├── Concept Drift     → real world relationships between variables changed
├── Accuracy Drop     → model predictions getting worse over time
├── New Data          → better/more data is now available
└── Business Changes  → new requirements old rules didn't account for
```

## Who Owns What

```
│
├── Data Collection          → Data Engineer
├── Data Preparation         → Data Analyst
└── Data Preprocessing       → Data Scientist + ML Engineer
        │
        ├── Initial Training          → Data Scientist
        ├── Continuous Learning       → Data Scientist + ML Engineer
        ├── Partial Retraining        → Data Scientist + ML Engineer
        ├── Full Model Retraining     → Data Scientist
        └── Inference Preprocessing   → ML Engineer
```