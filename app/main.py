from fastapi import FastAPI

from app.schemas import USERDETAILS

app = FastAPI()

@app.post('/Create_User')
async def createuser(userdetails:USERDETAILS):
    response = f"User has been sucessfully created. {userdetails.USERNAME}"
    return response