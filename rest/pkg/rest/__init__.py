from fastapi import FastAPI
from pkg.rest.routers.root import router as root_router
from pkg.rest.routers.v1 import router as v1_router

app = FastAPI()
app.include_router(root_router)
app.include_router(v1_router, prefix='/v1')
