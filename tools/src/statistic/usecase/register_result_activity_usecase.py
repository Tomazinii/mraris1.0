


from uuid import uuid4
from src._shared.usecase.usecase_interface import UsecaseInterface
from src._shared.value_object.email import Email
from src.classroom.facade.classroom_facade_interface import ClassroomFacadeInterface
from src.classroom.usecases.get_activity_by_id_usecase_dto import OutputGetActivityByIdDto
from src.statistic.domain.entity.activity import ActivityData
from src.statistic.domain.entity.metrics import Metrics
from src.statistic.domain.entity.result_activity import ResultActivity
from src.statistic.repository.statistic_repository_interface import ResultActivityRepositoryInterface
from src.statistic.usecase.register_result_activity_usecase_dto import InputRegisterResultActivityUsecaseDto
from src.statistic.domain.entity.student import Student


class RegisterResultActivityUsecase(UsecaseInterface):
    
    def __init__(self, repository: ResultActivityRepositoryInterface, activity_facade: ClassroomFacadeInterface, student_facade: ClassroomFacadeInterface):
        self.repository = repository
        self.activity_facade = activity_facade
        self.student_facade = student_facade


    def execute(self, input: InputRegisterResultActivityUsecaseDto):
        verify = self.repository.verify(activity_id=input.activity_id, user_id=input.student_id, problem_id=input.problem_id)

        if verify:

            activity: OutputGetActivityByIdDto = self.activity_facade.get_activity_by_id_method(input=input.activity_id)
    
            result_activity = ResultActivity(id=input.id)
            
            activity_data = ActivityData(
                category=activity.category,
                classroom_id=activity.classroom_id,
                id=activity.id,
                problem=activity.problem[input.problem_id],
                problem_id=input.problem_id,
                solution=input.solution,
                time=activity.time,
            )
            result_activity.set_activity(activity=activity_data)
            result_activity.set_classroom_id(id=input.classroom_id)
            metrics = Metrics(
                errors=input.num_errors,
                id=str(uuid4()),
                num_attempt=input.num_atempet,
                num_backs=input.num_backs,
                time=input.time,
            )
            result_activity.set_mrplato_metrics(mrplato_metrics=metrics)


            student_facade = self.student_facade.get_student_by_id(input=input.student_id)
            student = Student(
                email=Email(student_facade.email),
                enrollment=student_facade.enrollment,
                id=input.student_id,
                name=student_facade.name,
            )



            result_activity.set_student(student=student)

            self.repository.create(input=result_activity)
            
            