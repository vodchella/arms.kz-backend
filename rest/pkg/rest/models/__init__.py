from pydantic import BaseModel


class DBEntity(BaseModel):
    id: str

    class Config:
        orm_mode = True


class NamedEntity(DBEntity):
    name: str
