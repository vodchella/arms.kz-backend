from datetime import datetime
from fastapi import APIRouter
from pkg.models.exercise import ExerciseForListing, ExerciseCategory
from typing import List

router = APIRouter()


@router.get('/list', response_model=List[ExerciseForListing])
async def list_exercises():
    return [
        ExerciseForListing(
            id='111',
            name='Бицепс на скамье Скотта',
            last_workout_date=datetime.utcnow(),
            category=ExerciseCategory(id='aaa', name='Бицепс')
        ),
        ExerciseForListing(
            id='222',
            name='Пронация',
            last_workout_date=datetime.utcnow(),
            category=ExerciseCategory(id='bbb', name='Предплечье')
        ),
    ]
