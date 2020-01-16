from pkg.models.workout import WorkoutBase, HandWork
from pydantic import BaseModel


class ExerciseHistoryBase(BaseModel):
    workout: WorkoutBase


class ExerciseHistoryBothHands(ExerciseHistoryBase):
    hands: HandWork
    approaches_count: int


class ExerciseHistorySeparateHands(ExerciseHistoryBase):
    left_hand: HandWork
    right_hand: HandWork
    approaches_count: int
