from fastapi import APIRouter
from pkg.utils.dynamic_import import dynamic_import
from pkg.utils.logger import DEFAULT_LOGGER

router = APIRouter()


def module_loaded(module_name, module):
    router.include_router(module.router, prefix=f'/{module_name}')
    DEFAULT_LOGGER.info(f'... /{module_name} router loaded')


dynamic_import('./pkg/rest/routers/v1',
               'pkg.rest.routers.v1',
               'Loading /v1 routers:',
               module_loaded)
