from pkg.rest.models.workout import WorkoutBase
from pydantic import BaseModel


class ExerciseHistoryBase(BaseModel):
    workout: WorkoutBase
    approaches: int


class ExerciseHistoryBothHands(ExerciseHistoryBase):
    pass
    # hands: HandWork


class ExerciseHistorySeparateHands(ExerciseHistoryBase):
    pass
    # left_hand: HandWork
    # right_hand: HandWork
