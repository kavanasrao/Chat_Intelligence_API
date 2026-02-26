from typing import Optional, Dict, List, Literal
from pydantic import BaseModel, Field


class AgentState(BaseModel) :

    raw_text : str

    extracted : Optional[Dict[str, Optional[str]]] = None

    missing_field  : List[str] = Field(default_factort = list)

    status : Literal['new', 'processing', 'done'] = 'new'



    



    