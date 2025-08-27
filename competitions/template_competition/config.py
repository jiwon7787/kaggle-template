from pathlib import Path

# プロジェクト(このフォルダ)を基準に統一
PROJECT = Path(__file__).resolve().parent

DATA = PROJECT / "data"
RAW = DATA / "raw"               # 生データ（train.csv 等）
PROCESSED = DATA / "processed"   # 前処理済み
OUTPUTS = PROJECT / "outputs"    # モデル/予測/ログ
OUTPUTS.mkdir(parents=True, exist_ok=True)

# よく使うパスのエイリアス（存在チェックは呼び出し側で）
TRAIN_CSV = RAW / "train.csv"
TEST_CSV  = RAW / "test.csv"
