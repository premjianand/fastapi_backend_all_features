from sqlalchemy import Integer,String,Column,Boolean,DateTime,Enum,func
from sqlalchemy.types import LargeBinary

from app.database.database import Base
from app.schemas import ROLE_ENUM

class Timestamp:
    created_ts = Column(DateTime, default=func.now(), nullable=False)
    updated_ts = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

class Users(Base,Timestamp):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(LargeBinary)
    email_id = Column(String)
    phone_number = Column(String)
    role = Column(Enum(ROLE_ENUM))
    is_active = Column(Boolean, default=True)