venv:
	python3 -m venv venv
	
test:
	python3 -m pytest tests -lvv -ra
	
black:
	python3 -m black --check tests/ src/

black_diff:
	python3 -m black --diff tests/ src/

blacked:
	python3 -m black tests/ src/

build_env:
	python3 -m venv build-env

build:
	python3 -m pip install -r build-requirements.txt
	python3 -m build

upload:
	python3 -m twine upload dist/*

clean:
	rm -rf test-venv 
	rm -rf build-env
