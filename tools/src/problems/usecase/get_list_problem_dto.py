

import datetime
from typing import Any, List
from pydantic import BaseModel

class OutputGetListProblemDto (BaseModel):
    id: str
    list_name: str
    slug: str
    list_problem: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    comentary: str
