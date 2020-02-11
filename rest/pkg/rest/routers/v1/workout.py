from fastapi import APIRouter, Depends, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db.models.workout import Workout
from pkg.db.services.common_service import CommonService
from pkg.db.services.workout_service import WorkoutService
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.workout import WorkoutFullDTO, WorkoutDTO
from pkg.rest.models.user import UserDTO
from typing import List

router = APIRouter()


@router.get('/{workout_id}/view', response_model=WorkoutFullDTO)
async def view(workout_id: str = Path(..., regex=REGEXP_ID),
               user: UserDTO = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(Workout.__table__, workout_id, user.id)
    workout = await WorkoutService.get(workout_id)
    exercises = await WorkoutService.get_exercises(workout_id)
    result = WorkoutFullDTO(workout=workout,
                            exercises=exercises)
    return result


@router.get('/list', response_model=List[WorkoutDTO])
async def list_workouts(user: UserDTO = Depends(CurrentUser.get)):
    return await WorkoutService.list(user.id)
