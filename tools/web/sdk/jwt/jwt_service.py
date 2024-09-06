from uuid import uuid4
from src._shared.services.jwt_service_interface import JwtServiceInterface
import jwt


class JwtService(JwtServiceInterface):



    @classmethod
    def encode(self, data, jwt_secret=None):
        algorithm="HS256"
        if jwt_secret is None:
            jwt_secret = str(uuid4())

        encoded_jwt = jwt.encode(data, jwt_secret, algorithm=algorithm)
        return encoded_jwt, jwt_secret

    
    @classmethod
    def decode(self, data: any, jwt_secret: str):
        algorithm="HS256"
        data = jwt.decode(data, jwt_secret, algorithms=algorithm)
        return data