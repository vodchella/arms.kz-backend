from datetime import datetime
from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.rest.models.exercise import ExerciseForListing, ExerciseCategory
from pkg.rest.models.exercise_history import ExerciseHistoryBothHands, ExerciseHistorySeparateHands
from pkg.rest.models.workout import WorkoutBase, HandWork
from pkg.db.services.exercise_service import ExerciseService
from typing import List, Union


router = APIRouter()


@router.get('/list', response_model=List[ExerciseForListing])
async def list_exercises():
    return await ExerciseService.list('TWRvTJ4GkUTP6dGr')


@router.get('/list-categories', response_model=List[ExerciseCategory])
async def list_exercises():
    return await ExerciseService.list_categories('TWRvTJ4GkUTP6dGr')


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
