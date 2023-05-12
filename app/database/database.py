from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..setting import config


engine = create_engine(config.sqlalchemy_database_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
