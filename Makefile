default: build test

build: src/*.cpp include/*.h bindings/*.cpp
	source venv/bin/activate && python setup.py install

test:
	bash run_test
