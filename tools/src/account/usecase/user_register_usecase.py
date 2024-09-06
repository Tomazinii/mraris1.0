


from src._shared.errors.bad_request import BadRequestError
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.domain.entity.user import User
from src.account.domain.factory.user_factory import UserFactory
from src.account.domain.permissions.user_permissions import UserPermission
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface
from src.account.usecase.user_register_usecase_dto import InputUserRegisterUsecaseDto


class UserRegisterUsecase(UsecaseInterface):

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputUserRegisterUsecaseDto):

        check_register = self.repository.check_register(input.email)

        if check_register:
            return None
        


        user = UserFactory.create(
            created_at=input.created_at,
            email=input.email,
            id=input.id,
            password=input.password,
            updated_at=input.updated_at,
            username=input.username,
        )



        if input.is_admin:
            user.set_is_admin(status=True)
            user_type = UserPermission.admin_user_permission()
            user.change_type_user(user_type=user_type)

        self.repository.create(user)
        