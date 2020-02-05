from pydantic import BaseModel


class TokenPayload(BaseModel):
    ver: int
    uid: str
    exp: int
    typ: str
    key: str
