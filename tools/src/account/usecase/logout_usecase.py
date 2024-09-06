

from src._shared.session.user_session_interface import UserSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface


class LogoutUsecase(UsecaseInterface):

    def __init__(self, session: UserSessionInterface):
        self.session = session

    async def execute(self, session_key):

        if session_key is not None:
            await self.session.delete(session_key=session_key)