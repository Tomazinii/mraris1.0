from typing import List
from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException,Response
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src.mrplato.usecase.back_mrplato_usecase_dto import InputBackMrplatoUsecaseDto
from src.mrplato.usecase.check_status_mrplato_usecase_dto import InputCheckStatusMrplatoUsecaseDto
from src.mrplato.usecase.get_options_usecase_dto import InputGetOptionsUsecaseDto
from src.mrplato.usecase.prover_usecase_dto import InputProverUsecaseDto
from web.adapters.http_adapter import http_adapter
from web.composers.mrplato.back_mrplato_composer import back_mrplato_composer
from web.composers.mrplato.check_status_mrplato_composer import check_status_mrplato_composer
from web.composers.mrplato.get_options_composer import get_options_composer
from web.composers.mrplato.prover_mrplato_composer import mrplato_composer
from web.composers.mrplato.restart_status_mrplato_composer import retart_status_mrplato_composer
from web.middlewares.authentication import authentication_middleware
from web.session.mrplato_session import cookie

mrplato_router = APIRouter()

class InputProverRoute(BaseModel):
    selected_proof_line_indexes: List[int] 
    pb_index: int
    list_index: str
    type_selected: str
    sel_rule: int 
    input_formula: str = ""
    total_or_partial: str = "total"
    selection: int = 0
    activity_id:str
    classroom_id:str
    problem: str
    user_id: str
    user_status: bool



class InputGetOptionRoute(BaseModel):
    selected_proof_line_indexes: List[int] 
    pb_index: int
    list_index: str
    type_selected: str
    problem: str
    sel_rule: int 
    total_or_partial: str = "total"



@mrplato_router.post("/prover", status_code=201)
async def prover(requests: Request, input: InputProverRoute, response: Response):

    try:
        await authentication_middleware(requests=requests)
        session_key = None
        if requests.cookies.get("mrplato_cookie"):
            session_key = cookie(requests)

        input = InputProverUsecaseDto(
            input_formula=input.input_formula,
            list_index=input.list_index,
            pb_index=input.pb_index,
            sel_rule=input.sel_rule,
            selected_proof_line_indexes=input.selected_proof_line_indexes,
            selection=input.selection,
            session_key=session_key,
            user_status=input.user_status,
            total_or_partial=input.total_or_partial,
            type_selected=input.type_selected,
            activity_id=input.activity_id,
            classroom_id=input.classroom_id,
            problem=input.problem,
            user_id=input.user_id
        )

        response = await http_adapter(request=requests, controller=mrplato_composer(), response=response, input=input)
                
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



class InputCheckStatusMrplatoRouter(BaseModel):
    problem: str



@mrplato_router.post("/check_status_mrplato", status_code=201)
async def check_status_mrplato(requests: Request, input: InputCheckStatusMrplatoRouter, response: Response):
    try:
        await authentication_middleware(requests=requests)
        session_key = None
        if requests.cookies.get("mrplato_cookie"):
            session_key = cookie(requests)

        input = InputCheckStatusMrplatoUsecaseDto(
            problem=input.problem,
            session_key=session_key
        )

        response = await http_adapter(request=requests, controller=check_status_mrplato_composer(), response=response, input=input)

        return response
            
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
    



@mrplato_router.get("/back_state_mrplato", status_code=200)
async def check_status_mrplato(requests: Request, response: Response):
    
    try:
        await authentication_middleware(requests=requests)
        session_key = None
        if requests.cookies.get("mrplato_cookie"):
            session_key = cookie(requests)

        input = InputBackMrplatoUsecaseDto(
            session_key=session_key
        )

        response = await http_adapter(request=requests, controller=back_mrplato_composer(), response=response, input=input)

        return response
            
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")






@mrplato_router.get("/restart_status_mrplato", status_code=200)
async def restart_status_mrplato(requests: Request, response: Response):
    try:
        await authentication_middleware(requests=requests)
        session_key = None
        if requests.cookies.get("mrplato_cookie"):
            session_key = cookie(requests)


        response = await http_adapter(request=requests, controller=retart_status_mrplato_composer(), response=response, input=session_key)

        return response
            
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")




@mrplato_router.post("/get_options", status_code=200)
async def get_options(requests: Request, input: InputGetOptionRoute, response: Response):
    try:
        await authentication_middleware(requests=requests)
        session_key = None
        if requests.cookies.get("mrplato_cookie"):
            session_key = cookie(requests)

        input = InputGetOptionsUsecaseDto(
            list_index=input.list_index,
            pb_index=input.pb_index,
            sel_rule=input.sel_rule,
            selected_proof_line_indexes=input.selected_proof_line_indexes,
            session_key=session_key,
            total_or_partial=input.total_or_partial,
            type_selected=input.type_selected,
            problem=input.problem
        )

        response = await http_adapter(request=requests, controller=get_options_composer(), response=response, input=input)

        return response
            
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
    