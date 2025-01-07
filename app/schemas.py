from pydantic import BaseModel

class USERDETAILS(BaseModel):
    USERNAME:str
    EMAILID:str
    PASSWORD:str

class DUMMY(BaseModel):
    D:str