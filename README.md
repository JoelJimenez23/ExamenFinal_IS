# ExamenFinal_IS

Run

python3 -m venv
source venv/bin/activate

pip install flask
pip install coverage

python app.py
python3 -m coverage run -m unittest test_app.py
python3 -m coverage report
