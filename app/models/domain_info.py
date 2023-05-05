from database import Base
from sqlalchemy import Column, String, Boolean, Integer


class DomainInfo(Base):
    __tablename__ = 'DomainInfo'
    name = Column(String)
    technologies = Column(String, default = '')