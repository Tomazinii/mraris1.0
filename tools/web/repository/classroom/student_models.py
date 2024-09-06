from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime

class StudentModel(Base):
    __tablename__ = 'student'
    id = Column(String, primary_key=True)
    enrollment = Column(String, nullable=False)
    classroom_id = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


