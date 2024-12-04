python3 -m venv venv
sourve venv/bin/active
pip install flask
pip install coverage
python app.py
python3 -m coverage run -m unittest test_app.py
python3 -m coverage report

