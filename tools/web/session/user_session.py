import datetime
import pickle
from typing import Any, Optional

from pydantic import BaseModel
from fastapi import HTTPException
from uuid import UUID, uuid4

from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.frontends.implementations import SessionCookie
from src._shared.session.user_session_dto import UserSessionDto
from src._shared.session.user_session_interface import UserSessionInterface


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


class BasicVerifier(SessionVerifier[str, UserSessionDto]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, Any],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model) -> bool:
        """If the session exists, it is valid"""
        return True

verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)

class UserSession(UserSessionInterface):

    async def create(self, jwt, jwt_secret, response, user_id):
        session_key = uuid4()

        data = UserSessionDto(
            id=session_key,
            user_id=user_id,
            time_session = datetime.datetime.now() + datetime.timedelta(weeks=5),
            token=jwt,
            token_key=jwt_secret
        )

        await backend.create(session_key, data)
        cookie.attach_to_response(response, session_key)

    async def get(self, session_key):
        session_data = await backend.read(session_key)
        return session_data
    
    async def delete(self, session_key):
        if await self.verify(session_key) is not None:
            await backend.delete(session_key)

        
    async def verify(self, session_key):
        if session_key is None:
            return None
        
        session_data = await backend.read(session_key)
        if session_data is None:
            return None
        
        if session_data.time_session < datetime.datetime.now():
            try:
                await self.delete(session_key)
                return None
            except:
                return None
        
        return session_data
        

        
            


