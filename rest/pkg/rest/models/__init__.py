from pydantic import BaseModel


class DBEntity(BaseModel):
    id: str


class NamedEntity(DBEntity):
    name: str
