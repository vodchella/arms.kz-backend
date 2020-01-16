from pydantic import BaseModel


class NamedEntity(BaseModel):
    id: str
    name: str
