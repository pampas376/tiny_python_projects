#!/usr/bin/env bash

set -eu -o pipefail

PRG="wc1.py"
for FILE in solution*.py; do
    echo "==> ${FILE} <==" 
    cp "$FILE" "$PRG"
    make test
done

echo "Done."
