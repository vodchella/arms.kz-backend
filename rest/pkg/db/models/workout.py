from pkg.db import Base
from sqlalchemy import Column, ForeignKey, String, DateTime


class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    date = Column(DateTime(timezone=True))
    comment = Column(String)
