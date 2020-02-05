from datetime import datetime
from pydantic import BaseModel


class TokenPayload(BaseModel):
    ver: int
    uid: str
    exp: datetime
    typ: str
    key: str
