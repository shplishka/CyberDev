from typing import List

from pydantic import BaseModel


class Domain(BaseModel):
    name: str
    technology: str

    class Config:
        orm_mode = True
