from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime

class ClassroomModel(Base):
    __tablename__ = 'classroom'
    id = Column(String, primary_key=True)
    class_name = Column(String, nullable=False)
    teacher_name = Column(String, nullable=False)
    teacher_id = Column(String, nullable=False)
    teacher_created = Column(DateTime, nullable=False)
    teacher_updated = Column(DateTime, nullable=False)
    teacher_email = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
