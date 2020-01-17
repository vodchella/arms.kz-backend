from pkg.db import Base
from sqlalchemy import Column, ForeignKey, String, DateTime, SmallInteger, Numeric, Integer


class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    date = Column(DateTime(timezone=True))
    comment = Column(String)


class WorkoutExercise(Base):
    __tablename__ = 'workout_exercises'

    id = Column(String, primary_key=True)
    workout_id = Column(String, ForeignKey('workouts.id'))
    exercise_id = Column(String, ForeignKey('exercises.id'))
    approaches = Column(SmallInteger)
    lh_weight = Column(Numeric)
    lh_value = Column(Integer)
    rh_weight = Column(Numeric)
    rh_value = Column(Integer)
    bh_weight = Column(Numeric)
    bh_value = Column(Integer)
