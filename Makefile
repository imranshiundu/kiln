# KILN — the maker's bench
#
# The library is Markdown; the tooling is two Python files and a
# test runner. This Makefile is the front door to all of it.

.PHONY: help firetest strict inventory check fixtures snapshot clean

help: ## show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

firetest: ## run the Fire Test over every skill
	python3 scripts/firetest.py

strict: ## Fire Test with warnings treated as failures
	python3 scripts/firetest.py --strict

inventory: ## print the library inventory (name, phase, words, trigger)
	python3 scripts/firetest.py --list

check: firetest ## the full pre-push bar (Fire Test + checker tests)
	bash tests/run.sh

fixtures: ## rebuild the mini fixture library
	python3 tests/build_fixtures.py

snapshot: ## regenerate the golden inventory snapshot (after metadata changes)
	python3 scripts/firetest.py --list --json > tests/golden/inventory.json
