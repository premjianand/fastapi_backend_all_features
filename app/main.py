import os
from fastapi import FastAPI

from app.schemas import USERDETAILS

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI application is running!"}

@app.post('/Create_User')
async def createuser(userdetails:USERDETAILS):
    response = {"message":f"User has been sucessfully created. {userdetails.USERNAME}"}
    return response

if __name__ == "__main__":
    import uvicorn

    # Use the PORT environment variable or default to 8000
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)