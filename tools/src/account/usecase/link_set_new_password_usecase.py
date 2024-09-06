import datetime
from uuid import uuid4
from src._shared.services.email_service_interface import EmailServiceInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src._shared.value_object.email import Email
from src.account.domain.entity.link_new_password import LinkNewPassword
from src.account.domain.repository.link_repository_password_interface import LinkPasswordRepositoryInterface
from src.account.usecase.link_set_new_password_dto import InputNewPasswordDto
from web.config import HOST

class LinkSetNewPasswordUsecase(UsecaseInterface):
    
    def __init__(self, email_service: EmailServiceInterface, repository: LinkPasswordRepositoryInterface):
        self.email_service = email_service
        self.repository = repository

    def execute(self, input: InputNewPasswordDto) -> None:
   
        subject = "Reset Password - Mraris"

        link = LinkNewPassword(
                    id=str(uuid4()),
                    time_expires=datetime.datetime.now() + datetime.timedelta(days=1)
                )
        email = Email(input.user_email)
        link.set_to(email=email)
        link_invite = f"{HOST}/set-password/{link.get_id()}/{input.user_email}"

        content = f""" 
        Hello Student,
        access the link and set your new password!

        Access: {link_invite}.
                    """
                
        self.email_service.send(content=content, subject=subject, to=link.get_to())

        self.repository.create(link)

        return None
