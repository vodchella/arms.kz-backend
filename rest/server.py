import copy
import pid
import sys
import tempfile
import yaml
import uvicorn
from pkg.config import CONFIG, CFG_FILE
from pkg.constants.version import SOFTWARE_VERSION
from pkg.utils.console import panic
from pkg.utils.errors import get_raised_error
from pkg.utils.logger import DEFAULT_LOGGER, LOG_CONFIG


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

    pid_file = f'armgym-rest-{port}'
    pid_dir = tempfile.gettempdir()
    pid_file_full = f'{pid_dir}/{pid_file}.pid'
    pid_ok = False
    try:
        with pid.PidFile(pid_file, piddir=pid_dir) as p:
            pid_ok = True

            secure_config = copy.deepcopy(CONFIG)
            secure_config['postgres']['pass'] = '*****'

            DEFAULT_LOGGER.info(f'{SOFTWARE_VERSION} starting, PID: {p.pid}, File: {pid_file_full}')
            DEFAULT_LOGGER.info(f'Config loaded from {CFG_FILE}:\n{yaml.dump(secure_config, default_flow_style=False)}')

            from pkg.rest import app

            @app.on_event("startup")
            async def startup_event():
                DEFAULT_LOGGER.info(f'REST server started on {host}:{port}\n')
            uvicorn.run(app, host=host, port=port, log_config=LOG_CONFIG)
    except:
        if pid_ok:
            raise
        else:
            DEFAULT_LOGGER.critical(f'Something wrong with {pid_file_full}. Maybe it\'s locked?')
