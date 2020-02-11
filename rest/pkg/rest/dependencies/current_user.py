from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pkg.db.services.user_service import UserService
from pkg.rest.models.user import UserDTO
from pkg.rest.services.jwt_service import JwtService
from starlette.status import HTTP_401_UNAUTHORIZED


auth_scheme = HTTPBearer()


async def _get_current_user(token: str, expected_token_type: str) -> UserDTO:
    error_message = 'Недействительный токен'
    payload = JwtService.validate_token(token, expected_token_type)
    if payload:
        user = await UserService.get_by_id(payload.uid)
        if user:
            if payload.key == user['token_key']:
                if user['is_active']:
                    return UserDTO(**user)
                else:
                    error_message = 'Пользователь заблокирован'
        else:
            error_message = 'Пользователь не существует'
    raise HTTPException(HTTP_401_UNAUTHORIZED, error_message)


class CurrentUser:
    @staticmethod
    async def get(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserDTO:
        return await _get_current_user(token.credentials, 'a')

    @staticmethod
    async def get_by_refresh_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserDTO:
        return await _get_current_user(token.credentials, 'r')
