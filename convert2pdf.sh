#!/usr/bin/env bash
set -euo pipefail

CSS_FILE="pdf.css"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is not installed" >&2
  exit 1
fi

if ! command -v weasyprint >/dev/null 2>&1; then
  echo "Error: weasyprint is not installed" >&2
  exit 1
fi

if [[ ! -f "$CSS_FILE" ]]; then
  echo "Error: $CSS_FILE not found in repository root" >&2
  exit 1
fi

shopt -s nullglob
files=( *.md )

if [[ ${#files[@]} -eq 0 ]]; then
  echo "No markdown files found in repository root"
  exit 0
fi

for file in "${files[@]}"; do
  output="${file%.*}.pdf"
  echo "Converting $file -> $output"
  pandoc \
    --pdf-engine=weasyprint \
    --css="$CSS_FILE" \
    -s "$file" \
    -o "$output"
done

echo "Done"
