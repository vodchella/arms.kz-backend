from fastapi import APIRouter
from pkg.constants.version import SOFTWARE_VERSION

router = APIRouter()


@router.get('/api/')
async def root():
    return {
        'software': SOFTWARE_VERSION,
    }
