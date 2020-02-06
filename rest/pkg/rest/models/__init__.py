from pydantic import BaseModel
from typing import Optional


class DBEntity(BaseModel):
    id: Optional[str]


class NamedEntity(DBEntity):
    name: str
