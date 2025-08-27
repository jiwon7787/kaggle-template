# Competition Template

## Structure
- `data/raw/`       : original data (NOT in git)
- `data/processed/` : features, cached artifacts (NOT in git)
- `outputs/`        : models, predictions, logs (NOT in git)
- `notebooks/`      : experiments
- `scripts/`        : reusable code
- `config.py`       : project-scoped paths

## Import in notebooks
```python
import sys
from pathlib import Path
PROJECT_ROOT = Path.home() / "MyKaggle"  # or your repo root
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# from competitions.<your_comp_name>.config import RAW, PROCESSED, OUTPUTS

