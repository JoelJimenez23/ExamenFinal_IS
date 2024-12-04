# ExamenFinal_IS

How to Run

python3 -m venv
source venv/bin/activate

pip install flask coverage

python app.py \n
python3 -m coverage run -m unittest test_app.py
python3 -m coverage report
