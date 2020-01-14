import logging
import sys
import traceback
from pkg.constants.error_codes import ERROR_CUSTOM_EXCEPTION, ERROR_TEXT_MAP
from pkg.constants.logging import REST_LOGGER_NAME
from starlette.responses import JSONResponse
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


def response_error(code: int,
                   message: str = None,
                   status_code: int = 500,
                   detail: List[Dict] = None,
                   default_logger: str = REST_LOGGER_NAME,
                   log_stacktrace: bool = True,
                   log_error: bool = True):

    msg = message if message else ERROR_TEXT_MAP[code]

    error_json = {'error': {'code': code, 'message': msg}}
    stacktrace_log_msg = ''

    if detail:
        error_json['error']['detail'] = detail

    if log_stacktrace:
        error_stacktrace = get_raised_error(True)
        stacktrace_log_msg = f'{error_stacktrace}\n' if error_stacktrace else ''

    log = f'{stacktrace_log_msg}'

    if log_error:
        log = f'Status {status_code}, JSON: {error_json}{log}\n'

    logger = logging.getLogger(default_logger)
    logger.error(log)

    return JSONResponse(content=error_json, status_code=status_code)
