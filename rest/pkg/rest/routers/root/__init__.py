from fastapi import APIRouter
from pkg.constants.version import SOFTWARE_VERSION

router = APIRouter()


@router.get('/')
async def root():
    return {
        'software': SOFTWARE_VERSION,
    }
