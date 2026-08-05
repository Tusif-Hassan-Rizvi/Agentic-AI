from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_url import URL_DATABASE

db_url=URL_DATABASE
engine=create_engine(db_url)
session=sessionmaker(autoflush=False, autocommit=False, bind=engine)