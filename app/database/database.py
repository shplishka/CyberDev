from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from setting import config
import schemes
import models

engine = create_engine(config.sqlalchemy_database_url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def save_domain_info(db: Session, info: schemes.Domain):
    domain_info_model = models.DomainInfo(**info.dict())
    db.add(domain_info_model)
    db.commit()
    db.refresh(domain_info_model)
    return domain_info_model