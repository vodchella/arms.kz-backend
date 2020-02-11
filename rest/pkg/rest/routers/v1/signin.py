import json
from fastapi import APIRouter, Query, HTTPException
from httpx import AsyncClient
from pkg.config import CONFIG
from pkg.constants.urls import URL_GOOGLE_TOKEN_INFO
from pkg.db import db
from pkg.db.services.user_service import UserService
from pkg.rest.models.token_pair import TokenPairDTO
from pkg.rest.models.user import UserDTO
from pkg.rest.services.jwt_service import JwtService
from pkg.utils.errors import CustomException
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND

router = APIRouter()


@router.post('/google', response_model=TokenPairDTO)
@db.transaction()
async def signin_by_google_token(google_token: str = Query(..., alias='token')):
    async with AsyncClient() as client:
        params = {'id_token': google_token}
        response = await client.get(URL_GOOGLE_TOKEN_INFO, params=params)
        if response.status_code == HTTP_200_OK:
            resp_body = json.loads(response.content)
            user_data = UserDTO(**resp_body)
            user = await UserService.get_by_email(user_data.email)
            if user is not None:
                if user['is_active']:
                    return await JwtService.create_token_pair(user['id'])
                else:
                    raise CustomException('Пользователь заблокирован')
            else:
                raise CustomException('Пользователь не зарегистрирован')
        else:
            raise CustomException('Неверный токен Google')


@router.post('/developer', response_model=TokenPairDTO)
@db.transaction()
async def signin_developer():
    if CONFIG['app']['type'] == 'dev':
        return await JwtService.create_token_pair('TWRvTJ4GkUTP6dGr')
    else:
        raise HTTPException(HTTP_404_NOT_FOUND, 'Not Found')
