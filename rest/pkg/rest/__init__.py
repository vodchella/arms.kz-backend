from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pkg.db import db
from pkg.config import CONFIG
from pkg.constants.error_codes import ERROR_UNHANDLED_EXCEPTION, ERROR_CUSTOM_EXCEPTION
from pkg.rest.routers.root import router as root_router
from pkg.rest.routers.v1 import router as v1_router
from pkg.utils.errors import CustomException, response_error, CustomHTTPException
from pkg.utils.logger import DEFAULT_LOGGER
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_400_BAD_REQUEST

app = FastAPI()
app.include_router(root_router)
app.include_router(v1_router, prefix='/api/v1')


@app.on_event('startup')
async def startup_event():
    await db.connect()
    DEFAULT_LOGGER.info(f'REST server started on {CONFIG["rest"]["listen_host"]}:{CONFIG["rest"]["listen_port"]}\n')


@app.on_event('shutdown')
async def shutdown():
    await db.disconnect()


@app.exception_handler(Exception)
async def unhandled_exceptions_handler(request: Request, exc: Exception):
    return response_error(
        ERROR_UNHANDLED_EXCEPTION,
        str(exc)
    )


@app.exception_handler(HTTPException)
async def http_exceptions_handler(request: Request, exc: HTTPException):
    return response_error(
        exc.status_code,
        str(exc.detail),
        exc.status_code,
        log_stacktrace=False
    )


@app.exception_handler(CustomHTTPException)
async def custom_http_exceptions_handler(request: Request, exc: CustomHTTPException):
    return response_error(
        exc.error_code,
        exc.detail,
        exc.http_error_code,
        log_stacktrace=False
    )


@app.exception_handler(ValidationError)
async def http_exceptions_handler(request: Request, exc: ValidationError):
    return response_error(
        ERROR_UNHANDLED_EXCEPTION,
        str(exc),
        HTTP_400_BAD_REQUEST,
        log_stacktrace=False
    )


@app.exception_handler(RequestValidationError)
async def http_exceptions_handler(request: Request, exc: RequestValidationError):
    return response_error(
        ERROR_UNHANDLED_EXCEPTION,
        str(exc),
        HTTP_400_BAD_REQUEST,
        log_stacktrace=False
    )


@app.exception_handler(CustomException)
async def http_exceptions_handler(request: Request, exc: CustomException):
    return response_error(
        ERROR_CUSTOM_EXCEPTION,
        str(exc.detail),
        HTTP_400_BAD_REQUEST
    )
