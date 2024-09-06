

from typing import List
from src._shared.errors.not_found import NotFoundError
from src.account.domain.entity.invite import InviteStudent
from src.classroom.domain.entity.classroom import Classroom
from src.classroom.domain.repository.classroom_repository_interface import ClassroomRepositoryInterface
from src.classroom.usecases.get_classroom_usecase_dto import ClassroomDto, OutputGetClassroomUsecaseDto
from web.repository.classroom.classroom_models import ClassroomModel
from web.repository.db.config.connection import DBConnectionHandler


class ClassroomRepository(ClassroomRepositoryInterface):

    @classmethod
    def create(self, input: Classroom):
        with DBConnectionHandler() as db:
            try:
                classroom = ClassroomModel(
                id = input.get_id(),
                class_name = input.get_name_class(),
                teacher_name = input.get_teacher().get_name(),
                teacher_id = input.get_teacher().get_id(),
                teacher_created = input.get_teacher().get_created_at(),
                teacher_updated = input.get_teacher().get_updated_at(),
                teacher_email = input.get_teacher().get_email(),
                created_at = input.get_created_at(),
                updated_at = input.get_updated_at()
                )
                db.session.add(classroom)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            

    @classmethod
    def delete(self, id):
        raise NotImplementedError
    
    @classmethod
    def get_by_id(self, id):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(ClassroomModel).filter_by(id=id).first()
                if data is None:
                    raise NotFoundError("Classroom not found")
                
                classroom = ClassroomDto(
                            class_name=data.class_name,
                            teacher_name=data.teacher_name,
                            created_at=data.created_at,
                            id=data.id,
                            teacher_email=data.teacher_email,

                            )
                
                return classroom

                
        except Exception as error:
            db.session.rollback()
            raise error
    
    @classmethod
    def get(self, teacher_id) -> List[ClassroomModel]:
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(ClassroomModel).filter_by(teacher_id=teacher_id).all()

                classrooms = [ ClassroomDto(
                            class_name=classroom.class_name,
                            teacher_name=classroom.teacher_name,
                            created_at=classroom.created_at,
                            id=classroom.id,
                            teacher_email=classroom.teacher_email,
                        ) for classroom in data]
                
                return classrooms

                
        except Exception as error:
            db.session.rollback()
            raise error
        
