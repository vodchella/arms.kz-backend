import logging
import sys
import traceback
from pkg.constants.error_codes import ERROR_CUSTOM_EXCEPTION, ERROR_TEXT_MAP
from pkg.constants.logging import REST_LOGGER_NAME
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED
from typing import Dict, List


class CustomException(Exception):
    def __init__(self, detail: str) -> None:
        self.error_code = ERROR_CUSTOM_EXCEPTION
        self.detail = detail


def get_raised_error(full: bool = False):
    info = sys.exc_info()
    if info[0] is None and info[1] is None and info[2] is None:
        return
    e = traceback.format_exception(*info)
    if full:
        return ''.join(e)
    else:
        return (e[-1:][0]).strip('\n')


IGNORED_HTTP_CODES = [HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, ]


def response_error(code: int,
                   message: str = None,
                   status_code: int = HTTP_500_INTERNAL_SERVER_ERROR,
                   detail: List[Dict] = None,
                   log_stacktrace: bool = True):

    msg = message if message else ERROR_TEXT_MAP[code]
    error_json = {'error': {'code': code, 'message': msg}}

    if detail:
        error_json['error']['detail'] = detail

    if status_code not in IGNORED_HTTP_CODES:
        if log_stacktrace:
            error_stacktrace = get_raised_error(True)
            log_msg = f'{error_stacktrace}\n' if error_stacktrace else ''
        else:
            log_msg = f'Status {status_code}, JSON: {error_json}\n'

        logger = logging.getLogger(REST_LOGGER_NAME)
        logger.error(log_msg)

    return JSONResponse(content=error_json, status_code=status_code)
