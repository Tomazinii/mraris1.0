


from typing import Any, List
from pydantic import BaseModel


class Rows(BaseModel):
    content: str
    type: str = "default"
    methods_used_info: str


class InputGetOptionsUsecaseDto(BaseModel):
    session_key: Any
    selected_proof_line_indexes: List[int] # this is the index of the selected rows
    pb_index: int
    list_index: str
    type_selected: str
    problem: str
    sel_rule: int 
    total_or_partial: str = "total"


class OutputGetOptionsUsecaseDto(BaseModel):
    type_output: str
    message: str 
    lines: List

