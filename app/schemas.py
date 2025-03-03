from pydantic import BaseModel
from enum import Enum


class RoleEnum(str,Enum):
    ADMIN="ADMIN"
    USER="USER"


class UserDetails(BaseModel):
    USERNAME:str
    EMAIL_ID:str
    PASSWORD:str
    FIRST_NAME:str
    LAST_NAME:str
    PHONE_NUMBER:str
    ROLE:RoleEnum


class LoginDetails(BaseModel):
    EMAIL_ID:str
    PASSWORD:str