from pkg.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship


class ExerciseCategory_(Base):
    __tablename__ = 'exercise_categories'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    name = Column(String)


class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    category_id = Column(String, ForeignKey('exercise_categories.id'))
    name = Column(String)
    both_hands = Column(Boolean)
    last_workout_date = Column(DateTime(timezone=True))

    category = relationship('ExerciseCategory_')
