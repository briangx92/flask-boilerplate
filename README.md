Run these commands once you clone the repo
Python3 -m venv venv

Source venv/bin/activate
INSIDE VIRTUAL ENVIRONMENT

Pip install -e .

Pip install -e ‘.[test]’

Export FLASK_APP=flask_boilerplate
Export FLASK_ENV=development
cd (project directory)
flask run
