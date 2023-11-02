#!/bin/bash

set $DEFAULT_PATH "atlassian_venv"
if [[ -z "$1" ]]
then
    VENV_PATH=$DEFAULT_PATH
else
    VENV_PATH=$1
fi
echo "Creating virtual environment at $1"

python -m venv $VENV_PATH
source $VENV_PATH/bin/activate
pip install -r requirements.txt