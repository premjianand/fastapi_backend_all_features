import os
from fastapi import FastAPI

from app.schemas import USERDETAILS

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI application is running XOXO !"}

@app.post('/Create_User')
async def createuser(userdetails:USERDETAILS):
    response = {"message":f"User has been sucessfully created. {userdetails.USERNAME}"}
    return response