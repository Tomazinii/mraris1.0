

import datetime
from src._shared.errors.bad_request import BadRequestError
from src._shared.usecase.usecase_interface import UsecaseInterface

from src.account.domain.entity.link_new_password import LinkNewPassword
from src.account.domain.repository.link_repository_password_interface import LinkPasswordRepositoryInterface


class CheckLinkResetPasswordUsecase(UsecaseInterface):

    def __init__(self, repository: LinkPasswordRepositoryInterface):
        self.repository = repository

    def execute(self, link_id: str):
        link = self.repository.get(id=link_id)
        if link.active == False:
            raise BadRequestError("invitation time has expired")

        if datetime.datetime.now() > link.time_expires:
            raise BadRequestError("invitation time has expired")



        