

from src._shared.services.jwt_service_interface import JwtServiceInterface
from src._shared.session.user_session_dto import UserSessionDto
from src._shared.session.user_session_interface import UserSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.usecase.check_authenticate_usecase_dto import OutputCheckAuthenticateUsecaseDto


class CheckAuthenticateUsecase(UsecaseInterface):

    def __init__(self, session: UserSessionInterface, service: JwtServiceInterface):
        self.session = session
        self.service = service

    async def execute(self, session_key) -> OutputCheckAuthenticateUsecaseDto:

     
        data_session = await self.session.verify(session_key=session_key)

        if data_session is not None:
            json_data = self.service.decode(data_session.token, data_session.token_key)
            output = OutputCheckAuthenticateUsecaseDto(
                data=json_data,
                is_authenticated=True
            )

            return output
        
        output = OutputCheckAuthenticateUsecaseDto(
                data=data_session,
                is_authenticated=False
        )

        return output


