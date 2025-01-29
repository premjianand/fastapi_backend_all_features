from sqlalchemy import Integer,String,Column,Boolean,DateTime,Enum
from sqlalchemy.types import BINARY

from app.database.database import Base
from app.schemas import ROLE_ENUM

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(BINARY)
    email_id = Column(String)
    phone_number = Column(String)
    role = Column(Enum(ROLE_ENUM))
    created_ts = Column(DateTime)
    updated_ts = Column(DateTime)
    is_active = Column(Boolean, default=True)