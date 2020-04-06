#!/bin/bash
echo "Setting env..."
source $PWD/.venv/bin/activate

echo "Creating SAM template..."
python3 $PWD/serverless_dynamic.py

echo "Validating template..."
sam validate -t $PWD/template.yaml

if [ $? -eq 0 ]; then
    echo DEU_BAO
else
    echo DEU_RUIM
fi
