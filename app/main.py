import os
from fastapi import FastAPI

from app.schemas import USERDETAILS,DUMMY
from app.functions import scraper
from app.functions import decorators

app = FastAPI()

@app.get("/")
@decorators.decorator1
@decorators.decorator2
def read_root():
    return {"message": "FastAPI application is running XOXO !"}

@app.post('/Create_User')
async def createuser(userdetails:USERDETAILS):
    response = {"message":f"User has been sucessfully created. {userdetails.USERNAME}"}
    return response

@app.post('/scraping')
async def scraping(detail:DUMMY):
    response = scraper.scrap(detail)
    return response