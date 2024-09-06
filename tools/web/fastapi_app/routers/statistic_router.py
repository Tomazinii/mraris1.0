
from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src.statistic.usecase.get_solved_activity_dto import InputGetSolvedActivityDto
from web.adapters.http_adapter import http_adapter
from web.composers.statistic.generate_hash_list_solution_composer import generate_hash_list_composer
from web.composers.statistic.get_solved_problem_composer import get_solved_activity_composer
from web.middlewares.authentication import authentication_middleware


statistic_router = APIRouter()

class InputGetSolvedActivity(BaseModel):
    activity_id: str
    user_id: str


@statistic_router.post("/get_solved_activity", status_code=200)
async def get_problem(requests: Request, input: InputGetSolvedActivity):
    try:
        await authentication_middleware(requests=requests)
        input = InputGetSolvedActivityDto(
            activity_id=input.activity_id,
            user_id=input.user_id
        )

        response = http_adapter(requests, get_solved_activity_composer(), input=input, response=None)

        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



class InputGenerateHashSolutions(BaseModel):
    activity_id: str
    user_id: str

@statistic_router.post("/generate-hash", status_code=200)
async def generate_hash_list_solution(requests: Request, input: InputGenerateHashSolutions):
    try:
        await authentication_middleware(requests=requests)
        input = InputGetSolvedActivityDto(
            activity_id=input.activity_id,
            user_id=input.user_id
        )

        response = http_adapter(requests, generate_hash_list_composer(), input=input, response=None)

        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
    