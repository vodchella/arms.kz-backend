from datetime import datetime
from pkg.rest.models import DBEntity
from pkg.rest.models.exercise import Exercise
from pydantic import BaseModel
from typing import List, Optional


class WorkoutExerciseBase(BaseModel):
    exercise: Exercise
    approaches: Optional[int]
    lh_weight: Optional[float]
    lh_value: Optional[int]
    rh_weight: Optional[float]
    rh_value: Optional[int]
    bh_weight: Optional[float]
    bh_value: Optional[int]


class WorkoutBase(DBEntity):
    date: datetime
    comment: Optional[str]


class Workout(WorkoutBase):
    exercises: List[WorkoutExerciseBase]
