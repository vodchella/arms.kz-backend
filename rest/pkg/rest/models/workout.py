from datetime import datetime
from pkg.rest.models import DBEntity
from pydantic import BaseModel
from typing import List, Optional


class WorkoutExercise(BaseModel):
    approaches: Optional[int]
    lh_weight: Optional[float]
    lh_value: Optional[int]
    rh_weight: Optional[float]
    rh_value: Optional[int]
    bh_weight: Optional[float]
    bh_value: Optional[int]


class WorkoutExerciseFull(WorkoutExercise):
    exercise_id: str
    exercise_name: Optional[str]


class Workout(DBEntity):
    date: datetime
    comment: Optional[str]


class WorkoutFull(BaseModel):
    workout: Workout
    exercises: List[WorkoutExerciseFull]
