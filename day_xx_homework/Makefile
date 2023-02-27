PR = poetry run

.PHONY: .black
.black:
	$(PR) black --check .

.PHONY: .isort
.isort:
	$(PR) isort --check .

.PHONY: .mypy
.mypy:
	$(PR) mypy .

.PHONY: .pylint
.pylint:
	$(PR) pylint */

.PHONY: lint
lint:
	$(MAKE) --keep-going .black .isort .mypy .pylint

.PHONY: test
test:
	$(PR) pytest .
