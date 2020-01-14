from fastapi import APIRouter, Path
from pkg.constants.regexp import REGEXP_ID

router = APIRouter()


@router.get('/{user_id}/list')
async def root(user_id: str = Path(..., regex=REGEXP_ID)):
    return {
        'user_id': user_id,
    }
