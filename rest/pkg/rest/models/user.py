from pkg.rest.models import DBEntity
from typing import Optional


class User(DBEntity):
    email: str
    name: Optional[str]
    picture: Optional[str]
    locale: Optional[str]
