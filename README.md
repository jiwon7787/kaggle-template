# Kaggle Competition Template (Flat)

## Structure
- `data/raw/` : original data (NOT in git)
- `data/processed/` : features, cached artifacts (NOT in git)
- `outputs/` : models, predictions, logs (NOT in git)
- `notebooks/` : experiments
- `scripts/` : reusable code
- `config.py` : project-scoped paths (import with `from config import RAW, OUTPUTS`)

## Quick Start
1. Create a repo from this template (GitHub "Use this template" or `gh repo create <you>/<new> --template <you>/kaggle-template`)
2. Put data files into `data/raw/`
3. In notebooks:
   ```python
   from config import RAW, PROCESSED, OUTPUTS

