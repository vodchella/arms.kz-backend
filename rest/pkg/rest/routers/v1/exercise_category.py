from fastapi import APIRouter, Depends, Body, Path
from pkg.constants.regexp import REGEXP_ID
from pkg.db import db
from pkg.db.models.exercise import ExerciseCategory
from pkg.db.services.common_service import CommonService
from pkg.db.services.exercise_category_service import ExerciseCategoryService
from pkg.db.services.exercise_service import ExerciseService
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.exercise import ExerciseCategoryDTO
from pkg.rest.models.user import UserDTO
from pkg.utils.errors import CustomException
from typing import List


router = APIRouter()


@router.get('/list', response_model=List[ExerciseCategoryDTO])
async def list_categories(user: UserDTO = Depends(CurrentUser.get)):
    return await ExerciseCategoryService.list(user.id)


@router.post('/create', response_model=ExerciseCategoryDTO)
@db.transaction()
async def create_category(data: ExerciseCategoryDTO = Body(...),
                          user: UserDTO = Depends(CurrentUser.get)):
    category_id = await ExerciseCategoryService.create(data, user.id)
    return await ExerciseCategoryService.get(category_id)


@router.post('/{category_id}/update', response_model=ExerciseCategoryDTO)
@db.transaction()
async def update_category(category_id: str = Path(..., regex=REGEXP_ID),
                          data: ExerciseCategoryDTO = Body(...),
                          user: UserDTO = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(ExerciseCategory.__table__, category_id, user.id)
    await ExerciseCategoryService.update(category_id, data)
    return await ExerciseCategoryService.get(category_id)


@router.delete('/{category_id}/delete')
@db.transaction()
async def delete_category(category_id: str = Path(..., regex=REGEXP_ID),
                          user: UserDTO = Depends(CurrentUser.get)):
    await CommonService.check_entity_belongs_to_user(ExerciseCategory.__table__, category_id, user.id)
    category = ExerciseCategoryDTO(** await ExerciseCategoryService.find_main(user.id))
    if category.id != category_id:
        await ExerciseService.move_exercises(category_id, category.id)
        await CommonService.delete_entity(ExerciseCategory.__table__, category_id)
        return True
    else:
        raise CustomException('Нельзя удалить основную категорию')
