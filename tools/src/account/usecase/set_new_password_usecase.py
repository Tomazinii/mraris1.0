from src._shared.errors.bad_request import BadRequestError
from src._shared.errors.unauthorized import UnauthorizedError
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.domain.entity.user import User
from src.account.domain.repository.link_repository_password_interface import LinkPasswordRepositoryInterface
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface
from src.account.domain.value_object.password import Password
from src.account.usecase.set_new_password_dto import InputSetNewPasswordDto


class NewPasswordUsecase(UsecaseInterface):

    def __init__(self, repository: UserRepositoryInterface, repository_link_password: LinkPasswordRepositoryInterface):
        self.repository = repository
        self.repository_link_password = repository_link_password

    def execute(self, input: InputSetNewPasswordDto):
        user: User = self.repository.get_by_email(input.user_email)
        link = self.repository_link_password.get(input.link_id)

        if link.active is False:
            raise BadRequestError("Invalid link")

        if link.to != input.user_email:
            raise UnauthorizedError("You are not allowed to change")
        new_password = Password(input.new_password)
        self.repository.change_password(user_id=user.get_id(), password=new_password.get_password())
        self.repository_link_password.stamp(input.link_id)
            
        


        