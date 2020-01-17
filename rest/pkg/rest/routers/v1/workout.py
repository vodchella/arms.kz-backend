from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db.services.workout_service import WorkoutService
from pkg.rest.models.workout import WorkoutBase, Workout
from typing import List

router = APIRouter()


@router.get('/{workout_id}/view', response_model=Workout)
async def view(workout_id: str = Path(..., regex=REGEXP_ID)):
    return await WorkoutService.view(workout_id)


@router.get('/list', response_model=List[WorkoutBase])
async def list_workouts():
    return await WorkoutService.list('TWRvTJ4GkUTP6dGr')
