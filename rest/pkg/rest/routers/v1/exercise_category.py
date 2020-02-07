from fastapi import APIRouter, Depends, Body, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db import db
from pkg.db.models.exercise import ExerciseCategory
from pkg.db.services.common_service import CommonService
from pkg.db.services.exercise_service import ExerciseService
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.exercise import ExerciseCategory as ExerciseCategoryDTO
from pkg.rest.models.user import User
from typing import List


router = APIRouter()


@router.get('/list', response_model=List[ExerciseCategoryDTO])
async def list_categories(user: User = Depends(CurrentUser.get)):
    return await ExerciseService.list_categories(user.id)


@router.post('/create', response_model=ExerciseCategoryDTO)
@db.transaction()
async def create_category(data: ExerciseCategoryDTO = Body(...),
                          user: User = Depends(CurrentUser.get)):
    data.id = await ExerciseService.create_category(data, user.id)
    return data


@router.post('/{category_id}/update', response_model=ExerciseCategoryDTO)
@db.transaction()
async def update_category(category_id: str = Path(..., regex=REGEXP_ID),
                          data: ExerciseCategoryDTO = Body(...),
                          user: User = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(ExerciseCategory.__table__, category_id, user.id)
    data.id = category_id
    await ExerciseService.update_category(data)
    return data