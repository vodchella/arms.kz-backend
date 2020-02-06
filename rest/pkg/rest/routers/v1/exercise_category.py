from fastapi import APIRouter, Depends, Body
from pkg.db import db
from pkg.db.services.exercise_service import ExerciseService
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.exercise import ExerciseCategory
from pkg.rest.models.user import User
from typing import List


router = APIRouter()


@router.get('/list', response_model=List[ExerciseCategory])
async def list_categories(user: User = Depends(CurrentUser.get)):
    return await ExerciseService.list_categories(user.id)


@router.post('/create', response_model=ExerciseCategory)
@db.transaction()
async def create_category(data: ExerciseCategory = Body(...),
                          user: User = Depends(CurrentUser.get)):
    data.id = await ExerciseService.create_category(data, user.id)
    return data
