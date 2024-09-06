from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

class ActivityModel(Base):
    __tablename__ = 'activity'
    id = Column(String, primary_key=True)
    category = Column(String, nullable=False)
    time = Column(DateTime(timezone=True), nullable=False)
    availability = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    list_problem = Column(ARRAY(String), nullable=False)
    problem_id = Column(String, nullable=False)
    problem_name = Column(String, nullable=False)
    problem_slug = Column(String, nullable=False)
    classroom_id = Column(String, ForeignKey('classroom.id'), nullable=False)
    classroom = relationship("ClassroomModel")





