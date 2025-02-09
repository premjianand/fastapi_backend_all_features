import os

from fastapi import FastAPI,Depends,status,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from datetime import datetime

from app.database.database import engine,get_db
from app.schemas import USERDETAILS, LOGINDETAILS
from app.database import models
from app.utilities import functions
from app.utilities.auth import AuthHandler

app = FastAPI()
models.Base.metadata.create_all(engine)

authhandler = AuthHandler()

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
            updated_ts = datetime.now(),
        ) 
        db.add(add_user_data)
        db.commit()
        response = {"message":f"User has been sucessfully created. {userdetails.USERNAME}"}
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=response
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"Error":e}
        )
    

@app.post('/Login')
async def login(login_credentials:LOGINDETAILS, db:Session=Depends(get_db)):
    try:
        email_id,password = login_credentials.EMAIL_ID, login_credentials.PASSWORD
        response = functions.check_credentials(email_id,password,db)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"response":response["response"],"token":response["token"]}
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"message": e.detail}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"Login Failed.":e}
        )
    
@app.get('/unprotected')
async def unprotected():
    return{"Hello World"}

@app.get('/protected')
async def protected(username=Depends(authhandler.auth_wraper)):
    return{"Username":username}