from src._shared.entity.base_entity import Base
from src._shared.errors.bad_request import BadRequestError
from src._shared.value_object.email import Email
from src.account.domain.permissions.user_permissions import UserPermission
from src.account.domain.value_object.password import Password




class User(Base):
    """_summary_

        the user_type can be: default; super_user; admin;
    """

    __username: str
    __email: Email
    __is_admin: bool = False
    __password: Password
    __is_super_user: bool = False
    __is_authenticated: bool = False
    __user_type: str = UserPermission.default_user_permission()

    def __init__(self, id, created_at, updated_at, username):
        super().__init__(id, created_at, updated_at)
        self.__username = username

    def set_password(self, password: Password):
            self.__password = password.get_password()

    def set_email(self, email: Email):
            self.__email = email.get_email()

    def change_password(self, new_password: Password):
        new_password.change_password(new_password=new_password)
        self.__password = new_password.get_password()

    def change_type_user(self, user_type: str):
        self.__user_type = user_type

    def set_is_admin(self, status: bool):
        self.__is_admin = status
        

    def set_super_user(self, status: bool):
        self.__is_super_user = status

    def verify_is_admin(self) -> bool:
        return self.__is_admin == True
    
    def verify_is_super_user(self) -> bool:
        return self.__is_super_user == True
    
    def verify_password_login(self, password_login: Password) -> bool:
        if not password_login.get_password() == self.get_password():
            raise BadRequestError("Email or password incorrect")

    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_is_authenticated(self):
        return self.__is_authenticated
    
    def get_is_super_user(self):
        return self.__is_super_user
    
    def get_is_admin(self):
        return self.__is_admin
    
    def get_user_type(self):
        return self.__user_type
    
    def authenticate_user(self, status: bool):
        self.__is_authenticated = status

    def deauthenticate_user(self):
        self.__is_authenticated = False
    
    def set_password_db(self, password: str):
        self.__password = password