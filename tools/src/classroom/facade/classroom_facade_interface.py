
from abc import ABC, abstractmethod
from src.classroom.facade.classroom_facade_dto import InputGetStudentFacadeDto, OutputGetClassroomByIdFacadeDto, OutputGetStudentFacadeDto



class ClassroomFacadeInterface(ABC):

    @abstractmethod
    def get_student_by_id(self, input: InputGetStudentFacadeDto) -> OutputGetStudentFacadeDto:
        raise NotImplementedError
    
    @abstractmethod
    def get_classroom_by_id_method(self, input) -> OutputGetClassroomByIdFacadeDto:
        raise NotImplementedError

    @abstractmethod
    def get_activity_by_id_method(self, input):
        raise NotImplementedError