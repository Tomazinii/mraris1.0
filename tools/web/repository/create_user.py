
import datetime
import hashlib
from uuid import uuid4
from web.repository.account.user_model import UserModel
from web.repository.db.config.connection import DBConnectionHandler


def create_user():

    with DBConnectionHandler() as db:
        try:
            password  = hashlib.sha256("adminrogerio".encode()).hexdigest()
            user_model = UserModel(
                id = str(uuid4()),
                username = "teste",
                email = "rogeriosalvini@ufg.br",
                created_at = datetime.datetime.now(),
                updated_at = datetime.datetime.now(),
                password = password,
                is_admin = True,
                is_super_user = True,
                is_authenticated = False,
                user_type = "admin"
            )
            db.session.add(user_model)
            db.session.commit()

        except Exception as error:
            db.session.rollback()
            raise error


create_user()