import json
from fastapi import APIRouter, Query
from httpx import AsyncClient
from pkg.constants.urls import URL_GOOGLE_TOKEN_INFO
from pkg.db.services.user_service import UserService
from pkg.rest.models.user import User
from pkg.utils.errors import CustomException
from starlette.status import HTTP_200_OK


router = APIRouter()


@router.post('/google', response_model=User)
async def register_by_google_token(google_token: str = Query(..., alias='token')):
    async with AsyncClient() as client:
        params = {'id_token': google_token}
        response = await client.get(URL_GOOGLE_TOKEN_INFO, params=params)
        if response.status_code == HTTP_200_OK:
            resp_body = json.loads(response.content)
            email = resp_body['email']
            user = await UserService.get_by_email(email)
            if user is None:
                user = await UserService.create(email,
                                                resp_body['name'],
                                                resp_body['picture'],
                                                resp_body['locale'])
                return user
            else:
                raise CustomException('Пользователь уже зарегистрирован')
        else:
            raise CustomException('Неверный токен Google')
