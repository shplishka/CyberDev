from ..database.database import Base
from sqlalchemy import Column, String, Integer


class DomainInfo(Base):
    __tablename__ = 'DomainInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default='')
    technology = Column(String, default='')
