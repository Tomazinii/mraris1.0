from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException,Response
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src.account.usecase.change_password_usecase_dto import InputChangePasswordDto
from src.account.usecase.link_set_new_password_dto import InputNewPasswordDto
from src.account.usecase.login_usecase_dto import InputLoginUsecase
from src.account.usecase.set_new_password_dto import InputSetNewPasswordDto
from web.adapters.http_adapter import http_adapter
from web.composers.account.change_password_composer import change_password_composer
from web.composers.account.check_composer import check_authentication_composer
from web.composers.account.check_link_reset_password_composer import check_link_reset_password_composer
from web.composers.account.link_reset_password_composer import link_reset_password_composer
from web.composers.account.login_composer import login_composer
from web.composers.account.logout_composer import logout_composer
from web.composers.account.reset_password_composer import reset_password_composer
from web.middlewares.authentication import authentication_middleware
from web.session.user_session import cookie

account_router = APIRouter()

class InputLoginRoute(BaseModel):
    email: str
    password: str


class InputChangePasswordRouteDto(BaseModel):
    password: str


@account_router.get("/logout", status_code=200)
async def logout(requests: Request):
    try:
        session_key = None
        if requests.cookies.get("user_cookie"):
            session_key = cookie(requests)

        response = await http_adapter(controller=logout_composer(), request=requests, input=session_key, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


@account_router.post("/login", status_code=200)
async def login(requests: Request, input: InputLoginRoute, response: Response):
    try:
        input = InputLoginUsecase(
            email=input.email,
            password=input.password,
        )

        response = await http_adapter(request=requests, controller=login_composer(), response=response, input=input)

        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


@account_router.post("/change-password", status_code=201)
async def change_password(requests: Request, input: InputChangePasswordRouteDto, response: Response):

    try:
        await authentication_middleware(requests=requests)

        session_key = None
        if requests.cookies.get("user_cookie"):
            session_key = cookie(requests)

        input = InputChangePasswordDto(
            new_password=input.password,
            session_key=session_key
        )
        response = await http_adapter(request=requests, controller=change_password_composer(), response=response, input=input)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")

@account_router.post("/link-forgot-password", status_code=201)
async def forgot_password(requests: Request, input: InputNewPasswordDto):

    try:
        response = http_adapter(request=requests, controller=link_reset_password_composer(), input=input, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



@account_router.post("/set-password", status_code=201)
async def set_new_password(requests: Request, input: InputSetNewPasswordDto):

    try:
        response = http_adapter(request=requests, controller=reset_password_composer(), input=input, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



class InputCheckLinkResetPassword(BaseModel):
    link_id: str

@account_router.post("/check-link-reset-password", status_code=200)
def check_link_reset_password(requests: Request, input: InputCheckLinkResetPassword):
    try:
        link_id = input.link_id
        response = http_adapter(controller=check_link_reset_password_composer(), request=requests, input=link_id, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


@account_router.get("/verify", status_code=200)
async def verify(requests: Request):

    try:
        session_key = None
        if requests.cookies.get("user_cookie"):
            session_key = cookie(requests)
   
        response = await http_adapter(request=requests, controller=check_authentication_composer(), response=None, input=session_key)

        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



