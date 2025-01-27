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
    PHONE_NUMBER:int
    ROLE:ROLE_ENUM