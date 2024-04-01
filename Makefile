venv:
	python3 -m venv venv
	./venv/bin/python3 -m pip install -r requirements.txt
	
test:
	python3 -m pytest tests -lvv -ra --junitxml=output.xml

test-env:
	python3 -m venv test-venv
	./test-venv/bin/python3 -m pip install -r requirements.txt

package_test : test-env
	./test-venv/bin/python3 -m pip install dist/*.whl
	./test-venv/bin/python3 -m pytest tests -lvv -ra
	
black:
	python3 -m black --check tests/ src/

black_diff:
	python3 -m black --diff tests/ src/

blacked:
	python3 -m black tests/ src/

build-env:
	python3 -m venv build-env
	./build-env/bin/python3 -m pip install -r build-requirements.txt

build : build-env
	./build-env/bin/python3 -m build

upload : build-env
	./build-env/bin/python3 -m twine upload dist/*

clean:
	rm -rf test-venv 
	rm -rf build-env
