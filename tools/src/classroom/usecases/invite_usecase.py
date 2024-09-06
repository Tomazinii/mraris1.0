import datetime
from uuid import uuid4
from src._shared.errors.bad_request import BadRequestError
from src._shared.services.email_service_interface import EmailServiceInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src._shared.value_object.email import Email
from src.account.domain.entity.invite import InviteStudent
from src.classroom.domain.repository.classroom_repository_interface import ClassroomRepositoryInterface
from src.classroom.usecases.invite_usecase_dto import InputInviteStudentDto
from web.config import HOST

class InviteStudentUsecase(UsecaseInterface):
    
    def __init__(self, email_service: EmailServiceInterface, repository: ClassroomRepositoryInterface):
        self.email_service = email_service
        self.repository = repository

    def execute(self, input: InputInviteStudentDto) -> None:
   
        subject = "Invitation mrplato register"

        students_email = [Email(email) for email in input.students_email]

        if students_email.__len__() > 0:
            for element in students_email:
                invite = InviteStudent(
                    classroom_id=input.classroom_id,
                    id=str(uuid4()),
                    time_expires=datetime.datetime.now() + datetime.timedelta(weeks=3)
                )
                invite.set_to(email=element)

                link_invite = f"{HOST}/invite/{invite.get_id()}/{invite.get_classroom_id()}"

                content = f""" 
    Hello Student,

    I hope all is well with you! I would like to take this opportunity to invite you to register on our online platform Mrplato.
    Our platform offers a variety of resources and tools that will help you maximize your learning and connect more efficiently with course content. With it, you will have access to complementary materials, discussion forums, interactive quizzes and much more!

    To register, just follow these simple steps:

    1. Access: {link_invite}.
    2. Fill out the registration form with your information.

    And ready! You will have immediate access to all resources available on our platform.

    If you have any questions or need assistance during the registration process, please don't hesitate to contact us. We are always available to help.

    We hope to see you soon on our platform!


                    """
                
                self.email_service.send(content=content, subject=subject, to=invite.get_to())

                self.repository.create(invite)

            return None

        raise BadRequestError("provide emails")