from datetime import datetime
from fastapi import APIRouter
from pkg.models.workout import WorkoutBase
from typing import List

router = APIRouter()


@router.get('/list', response_model=List[WorkoutBase])
async def root():
    return [
        WorkoutBase(
            id='qqq',
            workout_date=datetime.utcnow(),
            comment=''
        )
    ]
