from fastapi import APIRouter, Depends, Path, Body
from pkg.constants.regexp import REGEXP_ID
from pkg.db import db
from pkg.db.models.exercise import Exercise
from pkg.db.services.common_service import CommonService
from pkg.db.services.exercise_service import ExerciseService
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.exercise import ExerciseForListingDTO, ExerciseDTO
from pkg.rest.models.workout import WorkoutExerciseDTO
from pkg.rest.models.user import UserDTO
from typing import List


router = APIRouter()


@router.get('/list', response_model=List[ExerciseForListingDTO])
async def list_exercises(user: UserDTO = Depends(CurrentUser.get)):
    return await ExerciseService.list(user.id)


@router.post('/create', response_model=ExerciseDTO)
@db.transaction()
async def create_exercise(data: ExerciseDTO = Body(...),
                          user: UserDTO = Depends(CurrentUser.get)):
    exercise_id = await ExerciseService.create(data, user.id)
    return await ExerciseService.get(exercise_id)


@router.post('/{exercise_id}/update', response_model=ExerciseDTO)
@db.transaction()
async def update_category(exercise_id: str = Path(..., regex=REGEXP_ID),
                          data: ExerciseDTO = Body(...),
                          user: UserDTO = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(Exercise.__table__, exercise_id, user.id)
    await ExerciseService.update(exercise_id, data)
    return await ExerciseService.get(exercise_id)


@router.delete('/{exercise_id}/delete')
@db.transaction()
async def delete_category(exercise_id: str = Path(..., regex=REGEXP_ID),
                          user: UserDTO = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(Exercise.__table__, exercise_id, user.id)
    await CommonService.delete_entity(Exercise.__table__, exercise_id)
    return True


@router.get('/{exercise_id}/history', response_model=List[WorkoutExerciseDTO])
async def view_exercise_history(exercise_id: str = Path(..., regex=REGEXP_ID),
                                user: UserDTO = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(Exercise.__table__, exercise_id, user.id)
    return await ExerciseService.view_exercise_history(exercise_id)
