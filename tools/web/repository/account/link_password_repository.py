

from src._shared.errors.bad_request import BadRequestError
from src._shared.value_object.email import Email
from src.account.domain.entity.invite import InviteStudent
from src.account.domain.repository.link_repository_password_interface import LinkPasswordRepositoryInterface
from web.repository.account.link_password_model import LinkModel
from web.repository.db.config.connection import DBConnectionHandler


class LinkPasswordRepository(LinkPasswordRepositoryInterface):

    @classmethod
    def create(self, input: InviteStudent):
        with DBConnectionHandler() as db:
            try:
                invite = LinkModel(
                    id = input.get_id(),
                    to = input.get_to(),
                    time_expires = input.get_time_expires(),
                    active= input.get_active()
                )
                db.session.add(invite)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            
        
    @classmethod
    def stamp(self, id):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(LinkModel).filter_by(id=id).first()
                data.active = False
                db.session.commit()
            
        except Exception as error:
            db.session.rollback()
            raise error
        
    @classmethod
    def get(self, id):
        with DBConnectionHandler() as db:
            try:
                link_query = db.session.query(LinkModel).filter_by(id=id).first()
                if  link_query is None:
                    raise BadRequestError("Link not found")
               
                return link_query

            except Exception as error:
                db.session.rollback()
                raise error