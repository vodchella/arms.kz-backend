from fastapi import APIRouter, Depends, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db.models.exercise import Exercise
from pkg.db.services.common_service import CommonService
from pkg.db.services.exercise_service import ExerciseService
from pkg.db.services.workout_service import WorkoutService
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.exercise import ExerciseForListing
from pkg.rest.models.workout import WorkoutExerciseForListing
from pkg.rest.models.user import User
from typing import List


router = APIRouter()


@router.get('/list', response_model=List[ExerciseForListing])
async def list_exercises(user: User = Depends(CurrentUser.get)):
    return await ExerciseService.list(user.id)


@router.get('/{exercise_id}/history', response_model=List[WorkoutExerciseForListing])
async def view_exercise_history(exercise_id: str = Path(..., regex=REGEXP_ID),
                                user: User = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(Exercise.__table__, exercise_id, user.id)
    return await WorkoutService.view_exercise_history(exercise_id)
