import os

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database.database import engine,get_db
from app.schemas import USERDETAILS, LOGINDETAILS
from app.database import models
from app.utilities import functions

app = FastAPI()
models.Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return {"message": "FastAPI application is running XOXO !"}


@app.post('/Create_User')
async def createuser(userdetails:USERDETAILS, db:Session=Depends(get_db)):
    encrypted_password = functions.encrypt_password(userdetails.PASSWORD)
    try:
        add_user_data = models.Users(
            username = userdetails.USERNAME,
            first_name = userdetails.FIRST_NAME,
            last_name = userdetails.LAST_NAME,
            password = encrypted_password,
            email_id = userdetails.EMAIL_ID,
            phone_number = userdetails.PHONE_NUMBER,
            role = userdetails.ROLE,
            created_ts = datetime.now(),
            updated_ts = datetime.now(),
        ) 
        db.add(add_user_data)
        db.commit()
        response = {"message":f"User has been sucessfully created. {userdetails.USERNAME}"}
        return response
    except Exception as e:
        return "failed.", e
    

@app.post('/Login')
async def login(login_credentials:LOGINDETAILS, db:Session=Depends(get_db)):
    email_id,password = login_credentials.EMAIL_ID, login_credentials.PASSWORD
    response = functions.check_credentials(email_id,password,db)
    # response = ""
    return response