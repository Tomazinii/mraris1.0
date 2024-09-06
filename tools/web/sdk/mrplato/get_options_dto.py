

from typing import Any, List
from pydantic import BaseModel


class Rows(BaseModel):
    content: str
    type: str = "default"
    methods_used_info: str


class InputGetOptionDto(BaseModel):
    session_key: Any
    selected_proof_line_indexes: List[int] # this is the index of the selected rows
    type_selected: str
    sel_rule: int 
    total_or_partial: str = "total"


class OutputGetOptionDto(BaseModel):
    type_output: str
    message: str 
    prover_instance: Any
    lines: List[Rows]