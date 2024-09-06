

from src._shared.errors.bad_request import BadRequestError
from src._shared.value_object.email import Email
from src.account.domain.entity.invite import InviteStudent
from src.classroom.domain.repository.invite_repository_interface import InviteStudentRepositoryInterface
from web.repository.classroom.invite_models import InviteModel
from web.repository.db.config.connection import DBConnectionHandler


class InviteStudentRepository(InviteStudentRepositoryInterface):

    @classmethod
    def create(self, input: InviteStudent):
        with DBConnectionHandler() as db:
            try:
                invite = InviteModel(
                    id = input.get_id(),
                    to = input.get_to(),
                    time_expires = input.get_time_expires(),
                    classroom_id = input.get_classroom_id(),
                    active= input.get_active()
                )
                db.session.add(invite)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            
    @classmethod
    def get(self, id: str) -> InviteStudent:
        try:
            with DBConnectionHandler() as db:
                exist = db.session.query(InviteModel).filter_by(id=id).first() is not None

                if exist:
                    data = db.session.query(InviteModel).filter_by(id=id).first()
                    if data is not None:
                        invite = InviteStudent(
                            classroom_id=data.classroom_id,
                            id=data.id,
                            time_expires=data.time_expires,
                        )
                        invite.set_active(data.active)
                        email = Email(data.to)
                        invite.set_to(email=email)
                        return invite
                raise BadRequestError("Error getting invite")
            
        except Exception as error:
            db.session.rollback()
            raise error
        
    @classmethod
    def stamp(self, id):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(InviteModel).filter_by(id=id).first()
                data.active = False
                db.session.commit()
            
        except Exception as error:
            db.session.rollback()
            raise error
        
    classmethod
    def get_by_classroom(self, classroom_id: str):
        try:
            with DBConnectionHandler() as db:
                exist = db.session.query(InviteModel).filter_by(classroom_id=classroom_id).all() 
                if exist is None:
                    raise BadRequestError("Error getting invite")
                
                all_invites = []
                for data in exist:
                    invite = InviteStudent(
                        classroom_id=data.classroom_id,
                        id=data.id,
                        time_expires=data.time_expires,
                        )
                    invite.set_to(Email(data.to))
                    invite.set_active(data.active)
                    all_invites.append(invite)
              
                return all_invites
            
            
        except Exception as error:
            db.session.rollback()
            raise error