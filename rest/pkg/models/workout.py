from datetime import datetime
from pkg.models import DBEntity
from pkg.models.exercise import Exercise
from pydantic import BaseModel
from typing import List, Union


class HandWork(BaseModel):
    weight: float
    iterations_count: int


class WorkoutExerciseBase(BaseModel):
    exercise: Exercise
    approaches_count: int


class WorkoutExerciseBothHands(WorkoutExerciseBase):
    hands: HandWork


class WorkoutExerciseSeparateHands(WorkoutExerciseBase):
    left_hand: HandWork
    right_hand: HandWork


class WorkoutBase(DBEntity):
    workout_date: datetime
    comment: str


class Workout(WorkoutBase):
    exercises: List[Union[WorkoutExerciseBothHands, WorkoutExerciseSeparateHands]]
