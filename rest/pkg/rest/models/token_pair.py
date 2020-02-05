from pydantic import BaseModel


class TokenPair(BaseModel):
    auth: str
    refresh: str
