install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

format:
	black *.py

run:
	
	streamlit run /workspaces/project2_microservice/app.py  --server.enableCORS=false


test:
	python -m pytest -vv test_*.py


all: install format test run
