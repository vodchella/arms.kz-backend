from fastapi import APIRouter, Depends
from pkg.db import db
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.user import User
from pkg.rest.services.jwt_service import JwtService

router = APIRouter()


@router.get('/check')
async def check(user: User = Depends(CurrentUser.get)):
    return user


@router.post('/refresh')
@db.transaction()
async def refresh(user: User = Depends(CurrentUser.get_by_refresh_token)):
    return await JwtService.create_token_pair(user.id)
