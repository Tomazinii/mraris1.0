
from typing import List
from src._shared.errors.not_found import NotFoundError
from src._shared.value_object.email import Email
from src.classroom.domain.entity.student import Student
from src.classroom.domain.repository.student_repository_interface import StudentRepositoryInterface
from web.repository.classroom.classroom_models import ClassroomModel
from web.repository.classroom.student_models import StudentModel
from web.repository.db.config.connection import DBConnectionHandler


class StudentRepository(StudentRepositoryInterface):

    @classmethod
    def create(self, input: Student):
        with DBConnectionHandler() as db:
            try:
                student_model = StudentModel(
                    id = input.get_id(),
                    enrollment = input.get_enrollment(),
                    classroom_id = input.get_classroom_id(),
                    email = input.get_email(),
                    username = input.get_name(),
                    created_at = input.get_created_at(),
                    updated_at = input.get_updated_at()
                )
               
                db.session.add(student_model)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            


    @classmethod
    def get_by_id(self, id) -> Student:
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(StudentModel).filter_by(id=id).first()

                if element is None:
                    raise NotFoundError("Student not found")
 
                student = Student(
                    created_at=element.created_at,
                    enrollment=element.enrollment,
                    id=element.id,
                    name=element.username,
                    updated_at=element.updated_at,
                )
                student.set_classroom_id(element.classroom_id)
                email = Email(element.email)
                student.set_email(email=email)
                
                return student

        except Exception as error:
            db.session.rollback()
            raise error
    
    @classmethod
    def get(self, teacher_id) -> List[ClassroomModel]:
        pass

    @classmethod
    def get_all_by_classroom(self, classroom_id):
        try:
            with DBConnectionHandler() as db:
                    elements = db.session.query(StudentModel).filter_by(classroom_id=classroom_id).all()

                    if elements is None:
                        raise NotFoundError("Student not found")

                    student_list = []
                    for element in elements:
                        student = Student(
                            created_at=element.created_at,
                            enrollment=element.enrollment,
                            id=element.id,
                            name=element.username,
                            updated_at=element.updated_at,
                        )
                        student.set_classroom_id(element.classroom_id)
                        email = Email(element.email)
                        student.set_email(email=email)
                        student_list.append(student)
                    
                    return student_list

        except Exception as error:
            db.session.rollback()
            raise error
    
    @classmethod
    def verify_create(self, input: Student):
        with DBConnectionHandler() as db:
            try:
                verify_exists = db.session.query(StudentModel).filter_by(email=input.get_email()).first() 
                if verify_exists is not None:
                    verify_exists.classroom_id = input.get_classroom_id()
                    db.session.commit()
                    return None

                student_model = StudentModel(
                    id = input.get_id(),
                    enrollment = input.get_enrollment(),
                    classroom_id = input.get_classroom_id(),
                    email = input.get_email(),
                    username = input.get_name(),
                    created_at = input.get_created_at(),
                    updated_at = input.get_updated_at()
                )
               
                db.session.add(student_model)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            