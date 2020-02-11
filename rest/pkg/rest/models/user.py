from pkg.rest.models import DBEntity
from typing import Optional


class UserDTO(DBEntity):
    email: str
    name: Optional[str]
    picture: Optional[str]
    locale: Optional[str]
