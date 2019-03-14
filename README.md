Run these commands once you clone the repo
Python3 -m venv venv

Source venv/bin/activate
INSIDE VIRTUAL ENVIRONMENT

Pip install -e .

Pip install -e ‘.[test]’

export FLASK_APP=flask_boilerplate
export FLASK_ENV=development
cd (project directory)
flask run
Happy Dance :)
