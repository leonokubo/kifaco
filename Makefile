install:
	pip install -U pip
	pip install -U setuptools
	pip install pipenv
	pipenv install --system --deploy --ignore-pipfile

install-dev:
	pip install pipenv
	PIPENV_VENV_IN_PROJECT="enabled" pipenv install --dev --ignore-pipfile --clear

clean:
	@echo "Removendo arquivos *.pyc|__pycache__|coverage.xml ..."
	@find tests/ kifaco/ | egrep "*.pyc|*.pyo|__pycache__" | xargs rm -rf
	@rm -f ./coverage.xml
	@rm -f ./unit.xml

lint:
	black --check --verbose --py36 --line-length 120 kifaco
	autopep8 -i kifaco --recursive --select=E101,E121 --in-place

radon:
	radon cc -n A kifaco

pep8: clean
	@echo "Fazendo validação PEP8"
	@find kifaco/ -type f -name "*.py"| PIPENV_VERBOSITY=-1 xargs pipenv run flake8 --show-source --max-line-length=120 --ignore=E704,E402,W503 --max-complexity=9

tests: pep8
	@echo "Executando testes com coverage"
	@PIPENV_VERBOSITY=-1 TESTER_MODE=true pipenv run pytest tests --cov-report term --cov=kifaco --cov-report=xml --junit-xml=unit.xml -o junit_family=legacy

tests-unit: pep8
	@PIPENV_VERBOSITY=-1 pipenv run pytest --cov=kifaco tests/unit

clean-again:
	@echo "Removendo arquivos *.pyc|__pycache__ APÓS TESTS ..."
	@find tests/ kifaco/ | egrep "*.pyc|*.pyo|__pycache__" | xargs rm -rf
