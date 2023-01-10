from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


url = "mysql+pymysql://root:Bismillah19@localhost/wadb"

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
session = SessionLocal()

Base = declarative_base()

