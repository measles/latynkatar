venv:
	python3 -m venv venv
	
test:
	python3 -m pytest tests -lv -ra
	
black:
	python3 -m black --check tests/ latynkatar.py || python3 -m black --diff tests/ latynkatar.py
