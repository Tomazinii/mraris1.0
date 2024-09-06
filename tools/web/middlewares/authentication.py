from src._shared.errors.unauthorized import UnauthorizedError
from web.session.user_session import UserSession, cookie


async def authentication_middleware(requests):
    if not requests.cookies.get("user_cookie"):
        raise UnauthorizedError("You are not logged in")

    session_key = cookie(requests)
    session = UserSession()
    result = await session.verify(session_key=session_key)


    if result is None:
        raise UnauthorizedError("You are not logged in")
    
    return True
