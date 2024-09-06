from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class LinkModel(Base):
    __tablename__ = 'link_password'
    id = Column(String, primary_key=True)
    to = Column(String, nullable=False)
    time_expires = Column(DateTime, nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    