from fastapi import FastAPI
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import goodbye_pb2
import goodbye_pb2_grpc
import asyncio

app = FastAPI()

@app.get("/hello")
async def hello():
    async with grpc.aio.insecure_channel("grpc-hello:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(helloworld_pb2.HelloRequest(name="Leon"))
        return {"message": response.message}

@app.get("/goodbye")
async def goodbye():
    async with grpc.aio.insecure_channel("grpc-goodbye:50052") as channel:
        stub = goodbye_pb2_grpc.FarewellStub(channel)
        response = await stub.SayGoodbye(goodbye_pb2.GoodbyeRequest(name="Leon"))
        return {"message": response.message}
