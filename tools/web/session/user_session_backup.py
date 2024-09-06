import datetime
import pickle
from typing import Any, Optional

from pydantic import BaseModel
from fastapi import HTTPException
from uuid import UUID, uuid4
import redis
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.frontends.implementations import SessionCookie
from src._shared.session.user_session_dto import UserSessionDto
from src._shared.session.user_session_interface import UserSessionInterface
import aioredis

class CookieParameters(BaseModel):
    max_age: int = 14 * 24 * 60 * 60  # 14 days in seconds
    path: str = "/"
    domain: Optional[str] = None
    secure: bool = False
    httponly: bool = True
    samesite: Any

cookie_params = CookieParameters(samesite="None", secure=True)

cookie = SessionCookie(
    cookie_name="user_cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)
backend = InMemoryBackend[UUID, UserSessionDto]()


# class BasicVerifier(SessionVerifier[str, UserSessionDto]):
#     def __init__(
#         self,
#         *,
#         identifier: str,
#         auto_error: bool,
#         backend: InMemoryBackend[UUID, Any],
#         auth_http_exception: HTTPException,
#     ):
#         self._identifier = identifier
#         self._auto_error = auto_error
#         self._backend = backend
#         self._auth_http_exception = auth_http_exception

#     @property
#     def identifier(self):
#         return self._identifier

#     @property
#     def backend(self):
#         return self._backend

#     @property
#     def auto_error(self):
#         return self._auto_error

#     @property
#     def auth_http_exception(self):
#         return self._auth_http_exception

#     def verify_session(self, model) -> bool:
#         """If the session exists, it is valid"""
#         return True

# verifier = BasicVerifier(
#     identifier="general_verifier",
#     auto_error=True,
#     backend=backend,
#     auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
# )

class UserSession(UserSessionInterface):

    def redis_connect(self):
        r = redis.Redis(host='redis', port=6379, decode_responses=True)
        
        return r
    




    async def create(self, jwt, jwt_secret, response, user_id):
        session_key = uuid4()

        data = UserSessionDto(
            id=session_key,
            user_id=user_id,
            time_session = datetime.datetime.now() + datetime.timedelta(weeks=5),
            token=jwt,
            token_key=jwt_secret
        )

        redis = aioredis.from_url("redis://redis", decode_responses=True)

        data.id = str(data.id)
        data.time_session = data.time_session.isoformat()


        data_dict = data.model_dump(by_alias=True)

        await redis.hset("hash", mapping=data_dict)
        await redis.close()

        # await backend.create(session_key, data)
        cookie.attach_to_response(response, session_key)

    async def get(self, session_key):
        session_data = await backend.read(session_key)

        return session_data
    
    async def delete(self, session_key):
        if await self.verify(session_key) is not None:
            await backend.delete(session_key)

        
    async def verify(self, session_key):


        redis = aioredis.from_url("redis://redis",decode_responses=True)
        result = await redis.hgetall("hash")
        await redis.close()



    
        session_data = UserSessionDto(
            id=UUID(result["id"]),
            time_session=datetime.datetime.fromisoformat(result["time_session"]),
            token=result["token"],
            token_key=result["token_key"],
            user_id=result["user_id"],
        )


        print(session_data)
        if session_key is None:
            return None
        
        # session_data = await backend.read(session_key)
        if session_data is None:
            return None
        
        if session_data.time_session < datetime.datetime.now():
            try:
                await self.delete(session_key)
                return None
            except:
                return None
        
        return session_data
        

        
            


