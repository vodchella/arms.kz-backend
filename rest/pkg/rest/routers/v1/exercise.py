from datetime import datetime
from fastapi import APIRouter, Path, Depends
from pkg.db import SessionLocal
from pkg.db.models.exercise import Exercise
from pkg.constants.regexp import REGEXP_ID
from pkg.rest.models.exercise import ExerciseForListing, ExerciseCategory
from pkg.rest.models.exercise_history import ExerciseHistoryBothHands, ExerciseHistorySeparateHands
from pkg.rest.models.workout import WorkoutBase, HandWork
from sqlalchemy.orm import Session
from typing import List, Union

router = APIRouter()


def get(db: Session):
    return db.query(Exercise).all()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/list', response_model=List[ExerciseForListing])
async def list_exercises(db: Session = Depends(get_db)):
    return get(db)
    # return [
    #     ExerciseForListing(
    #         id='111',
    #         name='Бицепс на скамье Скотта',
    #         both_hands=False,
    #         last_workout_date=datetime.utcnow(),
    #         category=ExerciseCategory(id='aaa', name='Бицепс')
    #     ),
    #     ExerciseForListing(
    #         id='222',
    #         name='Пронация',
    #         both_hands=False,
    #         last_workout_date=datetime.utcnow(),
    #         category=ExerciseCategory(id='bbb', name='Предплечье')
    #     ),
    # ]


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
