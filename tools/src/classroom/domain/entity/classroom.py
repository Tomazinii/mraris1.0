

from src._shared.entity.base_entity import Base
from src.classroom.domain.entity.teacher import Teacher


class Classroom(Base):
    __class_name = str
    __teacher = Teacher

    def __init__(self, id, created_at, updated_at, class_name, teacher: Teacher):
        super().__init__(id, created_at, updated_at)
        self.__class_name = class_name
        self.__teacher= teacher
    
    def get_name_class(self):
        return self.__class_name
    
    def get_teacher(self):
        return self.__teacher

