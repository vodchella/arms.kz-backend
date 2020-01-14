from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.models.exercise import ExerciseOut
from typing import List

router = APIRouter()


@router.get('/{user_id}/list', response_model=List[ExerciseOut])
async def root(user_id: str = Path(..., regex=REGEXP_ID)):
    return [
        ExerciseOut(name='Бицепс'),
        ExerciseOut(name='Пронация'),
    ]
