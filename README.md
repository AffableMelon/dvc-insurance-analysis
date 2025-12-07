# Insurance Portfolio — EDA & Reproducible Pipeline

Overview This repository contains code, documentation and a reproducible data
pipeline to perform End-to-End Insurance Risk Analytics & Predictive Modeling for an insurance portfolio (Feb 2014 — Aug 2015). The repo is
structured for reproducibility using DVC and includes CI for basic checks.

Quickstart (local)

1. Clone the repo:

```bash
 git clone https://github.com/AffableMelon/dvc-insurance-analysis.git
 cd <dvc-insurance-analysis
```

2. Create a Python venv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux .venv\Scripts\activate      # Windows pip
pip install -r requirements.txt
```

4. Install DVC and initialize (if not already in repo):

```bash
pip install dvc
dvc init
```

5. Configure a local DVC remote:

```bash
mkdir -p ~/dvc-storage/insurance-portfolio dvc
remote add -d localstorage ~/dvc-storage/insurance-portfolio
```

6. Add your data to DVC:

```bash
# place CSV(s) in data/raw/, then:
dvc add data/raw/insurance_data.csv
git add data/raw/insurance_data.csv.dvc .gitignore
git commit -m "Add raw data to DVC tracking"
dvc push
```

## Repository layout

- src/: project source code (data loading, EDA scripts, plotting)
- data/raw/: raw data (DVC-tracked)
- data/processed/: outputs created by pipeline
- dvc.yaml: defines pipeline stages (prepare, eda, etc.)
- .github/workflows/ci.yml: GitHub Actions config
- tests/: pytest tests for small units

### DVC (recommended workflow)

- dvc init
- dvc remote add -d localstorage /path/to/local/storage
- dvc add data/raw/insurance_data.csv
- git add data/raw/insurance_data.csv.dvc
- git commit -m "Track raw data with DVC"
- dvc push

## CI

The included GitHub Actions workflow installs Python, installs dependencies,
runs linting and tests, and attempts `dvc pull` to ensure data is present on
the runner if configured.
