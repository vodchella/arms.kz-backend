from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pkg.db import db
from pkg.db.services.user_service import UserService
from pkg.rest.models.user import User
from pkg.rest.services.jwt_service import JwtService
from starlette.status import HTTP_401_UNAUTHORIZED

router = APIRouter()
auth_scheme = HTTPBearer()


async def _get_current_user(token: str, expected_token_type: str) -> User:
    error_message = 'Недействительный токен'
    payload = JwtService.validate_token(token, expected_token_type)
    if payload:
        user = await UserService.get_by_id(payload.uid)
        if user:
            if payload.key == user['token_key']:
                if user['is_active']:
                    return User(**user)
                else:
                    error_message = 'Пользователь заблокирован'
        else:
            error_message = 'Пользователь не существует'
    raise HTTPException(HTTP_401_UNAUTHORIZED, error_message)


async def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    return await _get_current_user(token.credentials, 'a')


async def get_current_user_by_refresh_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> User:
    return await _get_current_user(token.credentials, 'r')


@router.get('/check')
async def check(current_user: User = Depends(get_current_user)):
    return current_user


@router.post('/refresh')
@db.transaction()
async def refresh(current_user: User = Depends(get_current_user_by_refresh_token)):
    return await JwtService.create_token_pair(current_user.id)
