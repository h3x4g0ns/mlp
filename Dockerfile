FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
    libgl1-mesa-dev \
    libglib2.0-0

WORKDIR /app

COPY ./mlp /app/mlp
COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 42069

CMD ["python", "mlp/src/server.py"]