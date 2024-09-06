from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime,ARRAY

class ProblemModel(Base):
    __tablename__ = 'problem'

    id = Column(String, primary_key=True)
    list_name = Column(String, nullable=False)
    list_problem = Column(ARRAY(String), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    slug = Column(String, nullable=False)
    comentary = Column(String, nullable=True)



