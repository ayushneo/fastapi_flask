from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACLHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Ayush@0307@localhost:3306/Playground"

engine = create_engine(
    SQLACLHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
