from pkg.db import Base
from sqlalchemy import Column, String, Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String)
    name = Column(String)
    picture = Column(String)
    locale = Column(String)
    is_active = Column(Boolean)
