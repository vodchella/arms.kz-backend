import json
from fastapi import APIRouter, Query
from httpx import AsyncClient
from pkg.db.services.user_service import UserService
from pkg.utils.errors import CustomException
from starlette.status import HTTP_200_OK


router = APIRouter()


@router.post('/google')
async def register_by_google_token(google_token: str = Query(..., alias='token')):
    async with AsyncClient() as client:
        params = {'id_token': google_token}
        response = await client.get('https://oauth2.googleapis.com/tokeninfo', params=params)
        if response.status_code == HTTP_200_OK:
            resp_body = json.loads(response.content)
            email = resp_body['email']
            user = await UserService.get_by_email(email)
            if user is None:
                pass
            else:
                raise CustomException('Пользователь уже зарегистрирован')
            return resp_body
    return None
