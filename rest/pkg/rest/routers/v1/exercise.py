from datetime import datetime
from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.models.exercise import ExerciseOut, ExerciseCategory
from typing import List

router = APIRouter()


@router.get('/{user_id}/list', response_model=List[ExerciseOut])
async def root(user_id: str = Path(..., regex=REGEXP_ID)):
    return [
        ExerciseOut(
            id='111',
            name='Бицепс на скамье Скотта',
            last_workout_date=datetime.utcnow(),
            category=ExerciseCategory(id='aaa', name='Бицепс')
        ),
        ExerciseOut(
            id='222',
            name='Пронация',
            last_workout_date=datetime.utcnow(),
            category=ExerciseCategory(id='bbb', name='Предплечье')
        ),
    ]
