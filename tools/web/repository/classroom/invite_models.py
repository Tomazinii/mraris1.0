from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class InviteModel(Base):
    __tablename__ = 'invite_student'
    id = Column(String, primary_key=True)
    to = Column(String, nullable=False)
    time_expires = Column(DateTime, nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    classroom_id = Column(String, ForeignKey('classroom.id'), nullable=False)
    classroom = relationship("ClassroomModel")
    