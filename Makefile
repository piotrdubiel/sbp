default: build test

build: src/*.cpp include/*.h python/*.cpp
	source venv/bin/activate && python setup.py install

test:
	source venv/bin/activate && nosetests
