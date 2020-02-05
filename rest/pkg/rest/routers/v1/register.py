import json
from fastapi import APIRouter, Query
from httpx import AsyncClient
from starlette.status import HTTP_200_OK


router = APIRouter()


@router.post('/google')
async def register_by_google_token(google_token: str = Query(..., alias='token')):
    async with AsyncClient() as client:
        params = {'id_token': google_token}
        response = await client.get('https://oauth2.googleapis.com/tokeninfo', params=params)
        if response.status_code == HTTP_200_OK:
            resp_body = json.loads(response.content)
            return resp_body
    return None
