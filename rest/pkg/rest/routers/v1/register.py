import json
from fastapi import APIRouter, Query
from httpx import AsyncClient
from pkg.constants.urls import URL_GOOGLE_TOKEN_INFO
from pkg.db import db
from pkg.db.services.exercise_category_service import ExerciseCategoryService
from pkg.db.services.user_service import UserService
from pkg.rest.models.token_pair import TokenPairDTO
from pkg.rest.models.user import UserDTO
from pkg.rest.services.jwt_service import JwtService
from pkg.utils.errors import CustomException
from starlette.status import HTTP_200_OK


router = APIRouter()


@router.post('/google', response_model=TokenPairDTO)
@db.transaction()
async def register_by_google_token(google_token: str = Query(..., alias='token')):
    async with AsyncClient() as client:
        params = {'id_token': google_token}
        response = await client.get(URL_GOOGLE_TOKEN_INFO, params=params)
        if response.status_code == HTTP_200_OK:
            resp_body = json.loads(response.content)
            user_data = UserDTO(**resp_body)
            user = await UserService.get_by_email(user_data.email)
            if user is None:
                user_id = await UserService.create(user_data)
                await ExerciseCategoryService.create_default_category(user_id)
                return await JwtService.create_token_pair(user_id)
            else:
                raise CustomException('Пользователь уже зарегистрирован')
        else:
            raise CustomException('Неверный токен Google')
