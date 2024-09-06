import datetime
import pickle
from typing import Any, Optional

from pydantic import BaseModel
from fastapi import HTTPException
from uuid import UUID, uuid4

from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from src._shared.errors.bad_request import BadRequestError
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from web.sdk.mrplato.resources import tools_file as tools


class CookieParameters(BaseModel):
    max_age: int = 14 * 24 * 60 * 60  # 14 days in seconds
    path: str = "/"
    domain: Optional[str] = None
    secure: bool = False
    httponly: bool = True
    samesite: Any

cookie_params = CookieParameters(samesite="None", secure=True)

cookie = SessionCookie(
    cookie_name="mrplato_cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)
backend = InMemoryBackend[UUID, MrplatoSessionDto]()


class BasicVerifier(SessionVerifier[str, MrplatoSessionDto]):
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

class MrplatoSession(MrplatoSessionInterface):

    async def create(self, response) -> MrplatoSessionDto:
        session_key = uuid4()
        prover_instance = tools.Prover()
        serialized_instance = pickle.dumps(prover_instance)

        dataSession = MrplatoSessionDto(
            id=session_key,
            prover=serialized_instance,
            time_session = datetime.datetime.now() + datetime.timedelta(weeks=1),
            timer = datetime.datetime.now(),
        )

        await backend.create(session_key, dataSession)
        cookie.attach_to_response(response, session_key)

        return dataSession

    async def get(self, session_key):
        session_data = await backend.read(session_key)
        return session_data
        
    
    async def delete(self, session_key):
        if session_key is not None:
            try:
                await backend.delete(session_key)
            except:
                pass


    
    async def update(self, session_key, data_session):
        await backend.update(session_key, data_session)


    async def restart(self, session_key, response):
        if session_key is not None:
            await backend.delete(session_key)
            return await self.create(response)
    
    
    async def verify(self, session_key, response):

        if session_key is None:
            return await self.create(response)
        
        session_data = await backend.read(session_key)

        if session_data is None:
            return await self.create(response)
        
        if session_data.time_session < datetime.datetime.now():
            await self.delete(session_key)
            return await self.create(response)
        
        return session_data
    



