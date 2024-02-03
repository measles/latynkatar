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
