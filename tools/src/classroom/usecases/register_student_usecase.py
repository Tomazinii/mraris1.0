from src._shared.usecase.usecase_interface import UsecaseInterface
from src._shared.value_object.email import Email
from src.account.facade.account_facade_dto import InputRegisterUserFacade
from src.account.facade.account_facade_interface import AccountFacadeInterface
from src.classroom.domain.entity.student import Student
from src.classroom.domain.repository.invite_repository_interface import InviteStudentRepositoryInterface
from src.classroom.domain.repository.student_repository_interface import StudentRepositoryInterface
from src.classroom.usecases.register_student_usecase_dto import InputRegisterStudentUsecaseDto


class RegisterStudentUsecase(UsecaseInterface):

    def __init__(self, repository: StudentRepositoryInterface, account_facade: AccountFacadeInterface, invite_repository: InviteStudentRepositoryInterface):
        self.repository = repository
        self.account_facade = account_facade
        self.invite_repository = invite_repository

    def execute(self, input: InputRegisterStudentUsecaseDto):

        student = Student(
            created_at=input.created_at,
            enrollment=input.enrollment,
            id=input.id,
            name=input.username,
            updated_at=input.updated_at,
            
        )
        email = Email(input.email)
        student.set_email(email)
        student.set_classroom_id(input.classroom_id)

        input_facade = InputRegisterUserFacade(
            created_at=input.created_at,
            email=input.email,
            id=input.id,
            is_admin=False,
            password=input.password,
            updated_at=input.updated_at,
            username=input.username,
        )

  
        
        self.account_facade.register_user(input=input_facade)
        self.repository.verify_create(student)
        self.invite_repository.stamp(input.invite_id)
