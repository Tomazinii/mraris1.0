
import datetime
from typing_extensions import Annotated
from uuid import uuid4
from fastapi import APIRouter,Request,HTTPException
from fastapi import File, UploadFile
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src._shared.errors.bad_request import BadRequestError
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from web.adapters.http_adapter import http_adapter
from web.composers.problems.delete_problem_composer import delete_problem_composer
from web.composers.problems.get_all_problem_composer import get_all_problem_composer
from web.composers.problems.get_problem_composer import get_problem_composer
from web.composers.problems.register_problem_composer import register_problem_composer
from web.middlewares.authentication import authentication_middleware
from web.middlewares.authorization import authorization_middleware

problem_router = APIRouter()



@problem_router.post("/register_problem", status_code=201)
async def register_problem(requests: Request,list_name:str, file: Annotated[UploadFile, File()], comentary:str=""):
    
    try:
        await authentication_middleware(requests=requests)
        await authorization_middleware(requests=requests)
        input = InputRegisterListProblemDto(
            id=str(uuid4()),
            created_at = datetime.datetime.now(), 
            updated_at = datetime.datetime.now(), 
            comentary=comentary,
            list_name=list_name,
            list_problem=file
        )
        response = http_adapter(requests, register_problem_composer(), input=input, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


@problem_router.get("/get_problem{problem_id}", status_code=200)
async def get_problem(requests: Request, problem_id: str):
    try:
        await authentication_middleware(requests=requests)
        response = http_adapter(requests, get_problem_composer(), input=problem_id, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
    

@problem_router.get("/get_all_problem", status_code=200)
async def get_problem(requests: Request):
    try:
        await authentication_middleware(requests=requests)
        response = http_adapter(requests, get_all_problem_composer(), input=None, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
    


@problem_router.delete("/delete_problem/{problem_id}", status_code=200)
async def delete_problem(requests: Request, problem_id: str):
    try:
        await authentication_middleware(requests=requests)
        await authorization_middleware(requests=requests)
        response = http_adapter(requests, delete_problem_composer(), input=problem_id, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")