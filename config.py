from pathlib import Path

PROJECT = Path(__file__).resolve().parent

DATA_DIR = PROJECT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EXTERNAL_DIR = DATA_DIR / "external"
OUTPUTS_DIR = PROJECT / "outputs"

for d in [RAW_DIR, PROCESSED_DIR, EXTERNAL_DIR, OUTPUTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

TRAIN_CSV = RAW_DIR / "train.csv"
TEST_CSV  = RAW_DIR / "test.csv"
