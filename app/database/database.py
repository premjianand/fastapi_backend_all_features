from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session

from app.config import config

username = config["DATABASE"]["USERNAME"]
password = config["DATABASE"]["PASSWORD"]
database = config["DATABASE"]["DATABASE"]
port = config["DATABASE"]["PORT"]
host = config["DATABASE"]["HOST"]

db_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(db_string, pool_size=20, max_overflow=0)

engine = create_engine(db_string, pool_size=20, max_overflow=0)

Base = declarative_base()
session = scoped_session(sessionmaker(bind=engine, autoflush=False))

def get_db():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.autoflush = False

    try:
        yield session
    except Exception as e:
        raise e
    finally:
        session.rollback()
        session.close()
