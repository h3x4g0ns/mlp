# mlp

lightweight ML inference server with sockets


## Installation 

Run the following commands to set up your environment.

```sh
conda create -n mlp_server python=3.11
conda activate mlp_server
pip install -r requirements.txt
```
## Getting Started

For running the server and client together run the following command:

```sh
python run.py

# basically runs the following commands under the hood
python mlp/src/server.py &
python examples/client.py
```

### Running unittests

For running unittests run the following command:

```sh
make test

# basically runs the following command under the hood
pytest
```
