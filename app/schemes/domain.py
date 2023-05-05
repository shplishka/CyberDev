from typing import List

from pydantic import BaseModel

class Domain(BaseModel):
    name:str
    technologies:List[str]