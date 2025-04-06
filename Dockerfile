FROM python:3.13.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ../protos ./protos

# Generate gRPC code for both .proto files
RUN python -m grpc_tools.protoc -I./protos \
    --python_out=./app \
    --grpc_python_out=./app \
    ./protos/helloworld.proto ./protos/goodbye.proto || true

WORKDIR /app/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
