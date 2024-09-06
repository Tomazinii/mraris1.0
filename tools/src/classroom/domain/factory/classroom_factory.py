

from src._shared.value_object.email import Email
from src.classroom.domain.entity.classroom import Classroom
from src.classroom.domain.entity.teacher import Teacher


class ClassroomFactory:

    @staticmethod
    def create(id: str, class_name: str, teacher_name: str, teacher_email: str, teacher_id:str, teacher_created, teacher_updated,created_at, updated_at) -> Classroom:

        teacher = Teacher(
            created_at=teacher_created,
            id=teacher_id,
            name=teacher_name,
            updated_at=teacher_updated
        )

        teacher.set_email(Email(teacher_email))

        classroom = Classroom(
            class_name=class_name,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            teacher=teacher
        )

        return classroom