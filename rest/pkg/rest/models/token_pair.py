from pydantic import BaseModel


class TokenPairDTO(BaseModel):
    auth: str
    refresh: str
