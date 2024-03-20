.PHONY: run

run:
	python mlp/src/server.py &
	python examples/client.py
