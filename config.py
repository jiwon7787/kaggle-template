from pathlib import Path

# このリポがプロジェクトのルート
PROJECT = Path(__file__).resolve().parent

# データと出力（リポ内で完結）
DATA = PROJECT / "data"
RAW = DATA / "raw"               # 生データ（train.csv 等）
PROCESSED = DATA / "processed"   # 前処理成果物
OUTPUTS = PROJECT / "outputs"    # モデル/予測/ログ
OUTPUTS.mkdir(parents=True, exist_ok=True)

# よく使うパスエイリアス（存在チェックは呼び出し側で）
TRAIN_CSV = RAW / "train.csv"
TEST_CSV  = RAW / "test.csv"
