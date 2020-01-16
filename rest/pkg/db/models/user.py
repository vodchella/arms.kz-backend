from pkg.db import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String)
