from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime,ARRAY, Integer, Interval

class ResultActivityModel(Base):
    __tablename__ = 'result_activity_model'

    id = Column(String, primary_key=True)
    classroom_id = Column(String, nullable=False)
    activity_category = Column(String, nullable=False)
    activity_id = Column(String, nullable=False)
    student_id= Column(String, nullable=False)
    student_name = Column(String, nullable=False)
    student_enrollment= Column(String, nullable=False)
    student_email= Column(String, nullable=False)
    time_mrplato = Column(Interval, nullable=False)
    num_attempts= Column(Integer, nullable=False)
    num_backs= Column(Integer, nullable=False)
    num_errors= Column(Integer, nullable=False)
    problem_id= Column(Integer, nullable=False)
    problem= Column(String, nullable=False)
    solution= Column(ARRAY(String), nullable=False)
    time_activity_expires = Column(DateTime, nullable=False)

