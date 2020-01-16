from datetime import datetime
from pkg.rest.models import DBEntity
from pkg.rest.models.exercise import Exercise
from pydantic import BaseModel
from typing import List, Union


class HandWork(BaseModel):
    weight: float
    iterations: int


class WorkoutExerciseBase(BaseModel):
    exercise: Exercise
    approaches: int


class WorkoutExerciseBothHands(WorkoutExerciseBase):
    hands: HandWork


class WorkoutExerciseSeparateHands(WorkoutExerciseBase):
    left_hand: HandWork
    right_hand: HandWork


class WorkoutBase(DBEntity):
    date: datetime
    comment: str


class Workout(WorkoutBase):
    exercises: List[Union[WorkoutExerciseBothHands, WorkoutExerciseSeparateHands]]
