"""This repository is intended for learning and experimenting with DevOps techniques"""

from fastapi import FastAPI
import random

@app.get("/helloworld")
async def hello_world():
    return {"message": "hello world"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,20000)}


