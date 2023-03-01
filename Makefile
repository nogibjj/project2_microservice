install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

run:
	streamlit run app.py --server.enableCORS=false

test:
	python -m pytest -vv test_*.py


all: install format test run
