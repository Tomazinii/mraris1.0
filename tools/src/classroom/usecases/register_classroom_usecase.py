

from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.domain.factory.classroom_factory import ClassroomFactory
from src.classroom.domain.repository.classroom_repository_interface import ClassroomRepositoryInterface
from src.classroom.usecases.register_classroom_usecase_dto import InputRegisterClassroomDto, OutputRegisterClassroomDto


class RegisterClassroomUsecase(UsecaseInterface):
    
    def __init__(self, repository: ClassroomRepositoryInterface):
        self.repository = repository

    def execute(self, input: InputRegisterClassroomDto):

        classroom = ClassroomFactory.create(
            class_name=input.class_name,
            created_at=input.created_at,
            id=input.id,
            teacher_created=input.teacher_created,
            teacher_id=input.teacher_id,
            teacher_email=input.teacher_email,
            teacher_name=input.teacher_name,
            teacher_updated=input.teacher_updated,
            updated_at=input.updated_at,
        )

        self.repository.create(classroom)

        output = OutputRegisterClassroomDto(
            class_name=input.class_name,
            created_at=input.created_at,
            id=input.id,
            teacher_email=input.teacher_email,
            teacher_name=input.teacher_name,
        )

        return output