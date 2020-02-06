from pkg.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship


class ExerciseCategory(Base):
    __tablename__ = 'exercise_categories'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    name = Column(String)
    is_deleted = Column(Boolean)


class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    category_id = Column(String, ForeignKey('exercise_categories.id'))
    name = Column(String)
    both_hands = Column(Boolean)
    last_workout_id = Column(String, ForeignKey('workouts.id'))
    is_deleted = Column(Boolean)

    category = relationship('ExerciseCategory')
