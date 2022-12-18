#! /bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Please install Python 3.' >&2
  exit 1
fi
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 workoutgenerator.py