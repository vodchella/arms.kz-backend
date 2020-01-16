from datetime import datetime
from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.models.exercise import ExerciseForListing, ExerciseCategory
from pkg.models.exercise_history import ExerciseHistoryBothHands, ExerciseHistorySeparateHands
from pkg.models.workout import WorkoutBase, HandWork
from typing import List, Union

router = APIRouter()


@router.get('/list', response_model=List[ExerciseForListing])
async def list_exercises():
    return [
        ExerciseForListing(
            id='111',
            name='Бицепс на скамье Скотта',
            both_hands=False,
            last_workout_date=datetime.utcnow(),
            category=ExerciseCategory(id='aaa', name='Бицепс')
        ),
        ExerciseForListing(
            id='222',
            name='Пронация',
            both_hands=False,
            last_workout_date=datetime.utcnow(),
            category=ExerciseCategory(id='bbb', name='Предплечье')
        ),
    ]


@router.get(
    '/{exercise_id}/history',
    response_model=List[Union[ExerciseHistoryBothHands, ExerciseHistorySeparateHands]]
)
async def exercise_history(exercise_id: str = Path(..., regex=REGEXP_ID)):
    return [
        ExerciseHistoryBothHands(
            workout=WorkoutBase(
                id='qqq',
                date=datetime.utcnow(),
                comment='Second workout',
            ),
            hands=HandWork(
                weight=52,
                iterations=3,
            ),
            approaches=4,
        ),
        ExerciseHistoryBothHands(
            workout=WorkoutBase(
                id='www',
                date=datetime.utcnow(),
                comment='First workout',
            ),
            hands=HandWork(
                weight=47,
                iterations=5,
            ),
            approaches=5,
        ),
    ]
