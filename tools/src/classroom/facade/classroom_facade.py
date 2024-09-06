from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.facade.classroom_facade_dto import OutputGetActivityByIdFacadeDto, OutputGetClassroomByIdFacadeDto
from src.classroom.facade.classroom_facade_interface import ClassroomFacadeInterface
from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface


class ClassroomFacade(ClassroomFacadeInterface):

    def __init__(self, get_student: UsecaseInterface = None, get_classrom_by_id: UsecaseInterface = None, get_activity_by_id: UsecaseInterface = None):
        self.get_student = get_student
        self.get_classroom_by_id = get_classrom_by_id
        self.get_activity_by_id = get_activity_by_id

    def get_student_by_id(self, input: InputProblemFacadeDto) -> OutputProblemFacadeDto:
        result = self.get_student.execute(input)
        return result
    
    def get_classroom_by_id_method(self, input) -> OutputGetClassroomByIdFacadeDto:
        result = self.get_classroom_by_id.execute(input)
        return result


    def get_activity_by_id_method(self, input) -> OutputGetActivityByIdFacadeDto:
        result = self.get_activity_by_id.execute(input)
        return result