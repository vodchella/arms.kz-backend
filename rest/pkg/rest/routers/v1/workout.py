from datetime import datetime
from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db.services.workout_service import WorkoutService
from pkg.rest.models.exercise import Exercise
from pkg.rest.models.workout import WorkoutBase, Workout, WorkoutExerciseSeparateHands, WorkoutExerciseBothHands, HandWork
from typing import List

router = APIRouter()


@router.get('/{workout_id}/view', response_model=Workout)
async def view(workout_id: str = Path(..., regex=REGEXP_ID)):
    return Workout(
        id=workout_id,
        date=datetime.utcnow(),
        comment='Generated workout',
        exercises=[
            WorkoutExerciseSeparateHands(
                exercise=Exercise(
                    id='111',
                    category_id='eee',
                    name='Бицепс на скамье Скотта',
                    both_hands=False,
                ),
                left_hand=HandWork(
                    weight=50,
                    iterations=6,
                ),
                right_hand=HandWork(
                    weight=52,
                    iterations=5,
                ),
                approaches=5,
            ),
            WorkoutExerciseBothHands(
                exercise=Exercise(
                    id='222',
                    category_id='rrr',
                    name='Строгий бицепс',
                    both_hands=True,
                ),
                hands=HandWork(
                    weight=52,
                    iterations=3,
                ),
                approaches=4,
            ),
        ]
    )


@router.get('/list', response_model=List[WorkoutBase])
async def list_workouts():
    return await WorkoutService.list('TWRvTJ4GkUTP6dGr')
