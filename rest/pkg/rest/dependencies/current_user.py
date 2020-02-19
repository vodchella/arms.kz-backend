from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pkg.constants.error_codes import ERROR_INVALID_TOKEN, ERROR_USER_IS_BLOCKED, ERROR_USER_DOESNT_EXISTS
from pkg.db.services.user_service import UserService
from pkg.rest.models.user import UserDTO
from pkg.rest.services.jwt_service import JwtService
from pkg.utils.errors import CustomHTTPException
from starlette.status import HTTP_403_FORBIDDEN


auth_scheme = HTTPBearer()


async def _get_current_user(token: str, expected_token_type: str) -> UserDTO:
    payload = JwtService.validate_token(token, expected_token_type)
    if payload:
        user = await UserService.get_by_id(payload.uid)
        if user:
            if payload.key == user['token_key']:
                if user['is_active']:
                    return UserDTO(**user)
                else:
                    raise CustomHTTPException(HTTP_403_FORBIDDEN, ERROR_USER_IS_BLOCKED)
        raise CustomHTTPException(HTTP_403_FORBIDDEN, ERROR_USER_DOESNT_EXISTS)
    raise CustomHTTPException(HTTP_403_FORBIDDEN, ERROR_INVALID_TOKEN)


class CurrentUser:
    @staticmethod
    async def get(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserDTO:
        return await _get_current_user(token.credentials, 'a')

    @staticmethod
    async def get_by_refresh_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> UserDTO:
        return await _get_current_user(token.credentials, 'r')
