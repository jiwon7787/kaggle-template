#!/usr/bin/env bash
set -euo pipefail
if [ $# -lt 1 ]; then
  echo "Usage: $0 <competition_slug>   (e.g. cmi_detect_behavior)"
  exit 1
fi

slug="$1"
base="$(cd "$(dirname "$0")/.." && pwd)"
src="$base/competitions/template_competition"
dst="$base/competitions/$slug"

if [ -e "$dst" ]; then
  echo "Error: $dst already exists"
  exit 1
fi

cp -r "$src" "$dst"
mkdir -p "$dst/data/raw" "$dst/data/processed" "$dst/outputs" "$dst/notebooks" "$dst/scripts"
sed -i "1i# Project: $slug" "$dst/config.py"

echo "Created $dst"
echo "Next:"
echo "  - Put data into: $dst/data/raw/"
echo "  - Start notebooks in: $dst/notebooks/"
