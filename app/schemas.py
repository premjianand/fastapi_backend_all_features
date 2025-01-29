from pydantic import BaseModel
from enum import Enum


class ROLE_ENUM(str,Enum):
    ADMIN="ADMIN"
    USER="USER"


class USERDETAILS(BaseModel):
    USERNAME:str
    EMAIL_ID:str
    PASSWORD:str
    FIRST_NAME:str
    LAST_NAME:str
    PHONE_NUMBER:str
    ROLE:ROLE_ENUM


class LOGINDETAILS(BaseModel):
    EMAIL_ID:str
    PASSWORD:str