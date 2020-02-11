from fastapi import APIRouter, Depends
from pkg.db import db
from pkg.rest.dependencies.current_user import CurrentUser
from pkg.rest.models.token_pair import TokenPairDTO
from pkg.rest.models.user import UserDTO
from pkg.rest.services.jwt_service import JwtService

router = APIRouter()


@router.get('/check', response_model=UserDTO)
async def check(user: UserDTO = Depends(CurrentUser.get)):
    return user


@router.post('/refresh', response_model=TokenPairDTO)
@db.transaction()
async def refresh(user: UserDTO = Depends(CurrentUser.get_by_refresh_token)):
    return await JwtService.create_token_pair(user.id)
