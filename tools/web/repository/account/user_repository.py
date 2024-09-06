from src._shared.errors.bad_request import BadRequestError
from src._shared.value_object.email import Email
from src.account.domain.entity.user import User
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface
from web.repository.account.user_model import UserModel
from web.repository.db.config.connection import DBConnectionHandler


class UserRepository(UserRepositoryInterface):

    @classmethod
    def create(self, user: User):

            with DBConnectionHandler() as db:
                try:
             
                    user_model = UserModel(
                        id = user.get_id(),
                        username = user.get_username(),
                        email = user.get_email(),
                        created_at = user.get_created_at(),
                        updated_at = user.get_updated_at(),
                        password = user.get_password(),
                        is_admin = user.get_is_admin(),
                        is_super_user = user.get_is_super_user(),
                        is_authenticated = user.get_is_authenticated(),
                        user_type = user.get_user_type()
                    )

                    db.session.add(user_model)
                    db.session.commit()
                except Exception as error:
                    db.session.rollback()
                    raise error
        
    
    def delete(self, id):
        return super().delete(id)
    
    def get_by_email(self, email) -> User:
        with DBConnectionHandler() as db:
            try:

                user_query = db.session.query(UserModel).filter_by(email=email).first()
                if  user_query is None:
                    raise BadRequestError("Email or password incorrect")
                user = User(
                    created_at=user_query.created_at,
                    id=user_query.id,
                    updated_at=user_query.updated_at,
                    username=user_query.username
                )
                email = Email(user_query.email)
                user.set_email(email)
                user.set_is_admin(user_query.is_admin)
                user.set_super_user(user_query.is_super_user)
                user.set_password_db(user_query.password)
                user.authenticate_user(user_query.is_authenticated)
                user.change_type_user(user_query.user_type)

                return user

            except Exception as error:
                db.session.rollback()
                raise error

    def get_by_id(self, id):
        with DBConnectionHandler() as db:
            try:

                user_query = db.session.query(UserModel).filter_by(id=id).first()
                if  user_query is None:
                    raise BadRequestError("User not found")
                user = User(
                    created_at=user_query.created_at,
                    id=user_query.id,
                    updated_at=user_query.updated_at,
                    username=user_query.username
                )
                email = Email(user_query.email)
                user.set_email(email)
                user.set_is_admin(user_query.is_admin)
                user.set_super_user(user_query.is_super_user)
                user.set_password_db(user_query.password)
                user.authenticate_user(user_query.is_authenticated)
                user.change_type_user(user_query.user_type)

                return user

            except Exception as error:
                db.session.rollback()
                raise error
    
    def check_register(self, email: str) -> bool:
        with DBConnectionHandler() as db:
            try:

                user_exists = db.session.query(UserModel).filter_by(email=email).first() is not None

                return user_exists
            
            except Exception as error:
                raise error
    
    def change_password(self, user_id: str, password: str):
        with DBConnectionHandler() as db:
            try:
                user_exists = db.session.query(UserModel).filter_by(id=user_id).first()
                if user_exists is None:
                    raise BadRequestError("User not found")
                
                user_exists.password = password
                db.session.commit()
     
            
            except Exception as error:
                raise error

    def update(self, user: User):
        return super().update(user)

    
    