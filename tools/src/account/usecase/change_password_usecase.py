


from src._shared.errors.unauthorized import UnauthorizedError
from src._shared.session.user_session_dto import UserSessionDto
from src._shared.session.user_session_interface import UserSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface
from src.account.domain.value_object.password import Password
from src.account.usecase.change_password_usecase_dto import InputChangePasswordDto


class ChangePasswordUsecase(UsecaseInterface):

    def __init__(self, repository: UserRepositoryInterface, session: UserSessionInterface):
        self.repository = repository
        self.session = session

    async def execute(self, input: InputChangePasswordDto):
 
        session_data: UserSessionDto = await self.session.verify(input.session_key)
 
        if session_data is not None:
            user_id = session_data.user_id
            new_password = Password(input.new_password)
            self.repository.change_password(user_id=user_id, password=new_password.get_password())
            
            return None

        raise UnauthorizedError("You are not allowed to change")


        