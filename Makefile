app: 
	python main.py

appc:
	cd __pycache__
	python main.cpython-37.opt-1.pyc
	
compile:
	python -O -m compileall ./


clean:
	del /F /Q .\__pycache__