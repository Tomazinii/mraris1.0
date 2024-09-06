


from src.account.usecase.check_authenticate_usecase import CheckAuthenticateUsecase
from web.controllers.account.check_user_controller import CheckUserController
from web.sdk.jwt.jwt_service import JwtService
from web.session.user_session import UserSession


def check_authentication_composer():
    service = JwtService()
    session = UserSession()
    usecase = CheckAuthenticateUsecase(session=session, service=service)
    controller = CheckUserController(usecase=usecase)

    return controller