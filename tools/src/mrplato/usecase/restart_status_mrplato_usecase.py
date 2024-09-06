

from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface


class RestartStatusMrplatoUsecase(UsecaseInterface):

    def __init__(self, session: MrplatoSessionInterface):
        self.session = session

    async def execute(self, session_key: any):
        await self.session.delete(session_key=session_key)