from web.repository.db.config.base import Base
from sqlalchemy import Column, String, DateTime,Boolean

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    password = Column(String, nullable=False)
    is_super_user = Column(Boolean, nullable=False)
    is_authenticated = Column(Boolean, nullable=False)
    is_admin = Column(Boolean, nullable=False)
    user_type = Column(String, nullable=False)
