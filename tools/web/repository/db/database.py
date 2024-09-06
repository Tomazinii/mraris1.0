from web.repository.db.config.base import Base

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)

