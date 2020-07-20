from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FTR(Base):
    __tablename__ = "ftr"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    source = Column(String)
    end = Column(String)
