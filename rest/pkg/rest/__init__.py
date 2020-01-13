from pkg.config import CONFIG
from fastapi import FastAPI
from pkg.constants.error_codes import ERROR_UNHANDLED_EXCEPTION, ERROR_CUSTOM_EXCEPTION
from pkg.rest.routers.root import router as root_router
from pkg.rest.routers.v1 import router as v1_router
from pkg.utils.errors import CustomException, response_error
from pkg.utils.logger import DEFAULT_LOGGER, REST_LOGGER
from starlette.exceptions import HTTPException
from starlette.requests import Request

app = FastAPI()
app.include_router(root_router)
app.include_router(v1_router, prefix='/v1')


@app.middleware("http")
async def request_handler(request: Request, call_next):
    body_from_request = b''
    async for chunk in request.stream():
        body_from_request += chunk

    try:
        body = '\nBODY: ' + body_from_request.decode('utf-8') if body_from_request else ''
    except:
        body = '\nBODY: <binary data>'
    user_agent = request.headers['user-agent'] if 'user-agent' in request.headers else ''
    auth = f'\nAUTH: {request.headers["authorization"]}' if 'authorization' in request.headers else ''
    args = f'\nARGS: {str(request.query_params)}' if request.query_params else ''
    log_body = f'{auth}{args}{body}'
    log_body = f'{log_body}\n' if log_body else ''
    log = f'{request.method} {request.url} from {request.client.host} {user_agent}{log_body}'
    REST_LOGGER.info(log)

    response = await call_next(request)
    return response


@app.on_event("startup")
async def startup_event():
    DEFAULT_LOGGER.info(f'REST server started on {CONFIG["rest"]["listen_host"]}:{CONFIG["rest"]["listen_port"]}\n')


@app.exception_handler(Exception)
async def unhandled_exceptions_handler(request: Request, exc: Exception):
    return response_error(ERROR_UNHANDLED_EXCEPTION, str(exc), log_error=False)


@app.exception_handler(HTTPException)
async def http_exceptions_handler(request: Request, exc: HTTPException):
    return response_error(exc.status_code, str(exc.detail), exc.status_code, log_stacktrace=False)


@app.exception_handler(CustomException)
async def http_exceptions_handler(request: Request, exc: CustomException):
    return response_error(ERROR_CUSTOM_EXCEPTION, str(exc.detail), log_error=False)
