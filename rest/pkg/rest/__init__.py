from pkg.config import CONFIG
from fastapi import FastAPI
from pkg.rest.routers.root import router as root_router
from pkg.rest.routers.v1 import router as v1_router
from pkg.utils.logger import DEFAULT_LOGGER

app = FastAPI()
app.include_router(root_router)
app.include_router(v1_router, prefix='/v1')


@app.on_event("startup")
async def startup_event():
    DEFAULT_LOGGER.info(f'REST server started on {CONFIG["rest"]["listen_host"]}:{CONFIG["rest"]["listen_port"]}\n')
