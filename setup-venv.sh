#!/usr/bin/env bash

if [[ -z "$(which python3)" ]]; then
    echo "python3 is not available - please install Python >= 3.6"
    exit 1
fi

if [[ "$(python3 -V |awk '{print $2}' |cut -d. -f2)" -lt "6" ]]; then
    echo "$(python3 -V) is less than 3.6 - please install Python >= 3.6"
    exit 1
fi

python3 -m venv venv

source venv/bin/activate

if [[ -f requirements.txt ]]; then
    pip3 install --upgrade pip
    pip3 install --requirement requirements.txt
fi

