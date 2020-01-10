import copy
import sys
import yaml
import uvicorn
from fastapi import FastAPI
from pkg.config import CONFIG, CFG_FILE
from pkg.constants.version import SOFTWARE_VERSION
from pkg.utils.console import panic
from pkg.utils.errors import get_raised_error
from pkg.utils.logger import DEFAULT_LOGGER, LOG_CONFIG

app = FastAPI()


@app.get('/')
async def root():
    return {
        'software': SOFTWARE_VERSION,
    }


def get_settings():
    try:
        _host = CONFIG['rest']['listen_host']
        _port = CONFIG['rest']['listen_port']
        _pg_host = CONFIG['postgres']['host']
        _pg_port = CONFIG['postgres']['port']
        _pg_user = CONFIG['postgres']['user']
        _pg_pass = CONFIG['postgres']['pass']
        _pg_db = CONFIG['postgres']['db']
        return _host, int(_port), _pg_host, _pg_port, _pg_user, _pg_pass, _pg_db
    except:
        DEFAULT_LOGGER.critical(get_raised_error(full=True))
        sys.exit(1)


if __name__ == "__main__":
    if sys.version_info < (3, 8):
        panic('We need minimum Python version 3.8 to run. Current version: %s.%s.%s' % sys.version_info[:3])

    host, port, pg_host, pg_port, pg_user, pg_pass, pg_db = get_settings()

    secure_config = copy.deepcopy(CONFIG)
    secure_config['postgres']['pass'] = '*****'

    DEFAULT_LOGGER.info(f'Config loaded from {CFG_FILE}:\n{yaml.dump(secure_config, default_flow_style=False)}')
    uvicorn.run(app, host=host, port=port, log_config=LOG_CONFIG)
