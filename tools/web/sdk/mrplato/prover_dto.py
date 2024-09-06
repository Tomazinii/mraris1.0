from typing import Any, List
from pydantic import BaseModel


class NewLine(BaseModel):
    content: str
    methods_used_info: str
    type: str = "default"

class Rows(BaseModel):
    content: str
    type: str = "default"
    methods_used_info: str



class InputProverDto(BaseModel):

    selected_proof_line_indexes: List[int] # this is the index of the selected rows
    type_selected: str
    sel_rule: int 
    input_formula: str = ""
    total_or_partial: str = "total"
    selection: int = 0




class OutputProverDto(BaseModel):
    """
        Type of data outPut.
        all mandatory 
    """
    type_output: str
    message: str 
    lines: List[NewLine]
    prover_instance: Any
