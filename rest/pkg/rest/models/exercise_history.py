from pkg.rest.models.workout import WorkoutBase, HandWork
from pydantic import BaseModel


class ExerciseHistoryBase(BaseModel):
    workout: WorkoutBase
    approaches: int


class ExerciseHistoryBothHands(ExerciseHistoryBase):
    hands: HandWork


class ExerciseHistorySeparateHands(ExerciseHistoryBase):
    left_hand: HandWork
    right_hand: HandWork
