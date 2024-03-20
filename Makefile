.PHONY: run test

run:
	python mlp/src/server.py &
	python examples/client.py

test:
	pytest
