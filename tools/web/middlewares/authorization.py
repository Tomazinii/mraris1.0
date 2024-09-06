from src._shared.errors.unauthorized import UnauthorizedError
from web.sdk.jwt.jwt_service import JwtService
from web.session.user_session import UserSession, cookie


async def authorization_middleware(requests):
    if not requests.cookies.get("user_cookie"):
        raise UnauthorizedError("You are not logged in")

    session_key = cookie(requests)
    session = UserSession()
    result = await session.verify(session_key=session_key)

    if result is None:
        raise UnauthorizedError("You are not logged in")
    
    jwt = JwtService.decode(jwt_secret=result.token_key, data=result.token)

    if not jwt["is_admin"] == "True":
        raise UnauthorizedError("You are not permission")

