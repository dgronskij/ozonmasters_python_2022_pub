PR = poetry run

.PHONY: all
all: | lint test
	true

.make-deps: poetry.lock
	poetry install
	@touch $@

.PHONY: .black
.black: .make-deps
	$(PR) black --check .

.PHONY: .isort
.isort: .make-deps
	$(PR) isort --check .

.PHONY: .mypy
.mypy: .make-deps
	$(PR) mypy .

.PHONY: .pylint
.pylint: .make-deps
	$(PR) pylint */

.PHONY: lint
lint: .make-deps
	$(MAKE) --keep-going .black .isort .mypy .pylint

.PHONY: test
test: .make-deps
	$(PR) pytest .

.PHONY: clean
clean:
	rm -rf \
		`find . -name '.*_cache'` \
		`find . -name '__pycache__'` \
		.make_* \
		.make-*
