


from src.account.facade.account_facade import AccountFacade
from src.account.usecase.user_register_usecase import UserRegisterUsecase
from src.classroom.usecases.register_student_usecase import RegisterStudentUsecase
from web.controllers.classroom.register_student_controller import RegisterStudentController
from web.repository.account.user_repository import UserRepository
from web.repository.classroom.invite_repository import InviteStudentRepository
from web.repository.classroom.student_repository import StudentRepository


def register_student_composer():
    repository_student = StudentRepository()
    repository_user = UserRepository()
    invite_repository = InviteStudentRepository()
    register_usecase = UserRegisterUsecase(repository=repository_user)
    account_facade = AccountFacade(register_usecase=register_usecase)
    usecase = RegisterStudentUsecase(repository=repository_student, account_facade=account_facade, invite_repository=invite_repository)
    controller = RegisterStudentController(usecase=usecase)
    return controller