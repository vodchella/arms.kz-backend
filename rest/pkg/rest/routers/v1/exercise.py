from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db.services.exercise_service import ExerciseService
from pkg.db.services.workout_service import WorkoutService
from pkg.rest.models.exercise import ExerciseForListing, ExerciseCategory
from pkg.rest.models.workout import WorkoutExerciseForListing
from typing import List


router = APIRouter()


@router.get('/list', response_model=List[ExerciseForListing])
async def list_exercises():
    return await ExerciseService.list('TWRvTJ4GkUTP6dGr')


@router.get('/list-categories', response_model=List[ExerciseCategory])
async def list_categories():
    return await ExerciseService.list_categories('TWRvTJ4GkUTP6dGr')


@router.get('/{exercise_id}/history', response_model=List[WorkoutExerciseForListing])
async def view_exercise_history(exercise_id: str = Path(..., regex=REGEXP_ID)):
    return await WorkoutService.view_exercise_history(exercise_id)
