

from src.account.usecase.login_usecase import LoginUsecase
from src.classroom.facade.classroom_facade import ClassroomFacade
from src.classroom.usecases.get_student_classroom_usecase import GetStudentUsecase
from web.controllers.account.login_controller import LoginController
from web.repository.account.user_repository import UserRepository
from web.repository.classroom.student_repository import StudentRepository
from web.sdk.jwt.jwt_service import JwtService
from web.session.user_session import UserSession


def login_composer():
    repository = UserRepository()
    service = JwtService()
    session = UserSession()
    repository_student = StudentRepository()
    get_student = GetStudentUsecase(repository=repository_student)
    classroom_facade = ClassroomFacade(get_student=get_student)
    usecase = LoginUsecase(repository=repository, service=service, session=session, classroom_facade=classroom_facade)
    controller = LoginController(usecase=usecase)
    return controller