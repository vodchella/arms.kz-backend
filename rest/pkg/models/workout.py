from datetime import datetime
from pkg.models import DBEntity
from pkg.models.exercise import Exercise
from pydantic import BaseModel
from typing import List


class WorkoutExercise(BaseModel):
    exercise: Exercise
    weight: float
    iterations_count: int
    approaches_count: int


class WorkoutBase(DBEntity):
    workout_date: datetime
    comment: str


class Workout(WorkoutBase):
    exercises: List[WorkoutExercise]
