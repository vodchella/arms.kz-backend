import copy
import pid
import sys
import tempfile
import yaml
import uvicorn
from pkg.config import CONFIG, CFG_FILE
from pkg.constants.version import SOFTWARE_VERSION
from pkg.utils.console import panic
from pkg.utils.logger import DEFAULT_LOGGER, LOG_CONFIG
from setproctitle import setproctitle


if __name__ == '__main__':
    if sys.version_info < (3, 8):
        panic('We need minimum Python version 3.8 to run. Current version: %s.%s.%s' % sys.version_info[:3])

    host = CONFIG['rest']['listen_host']
    port = int(CONFIG['rest']['listen_port'])

    proc_name = f'arms-rest-{port}'
    setproctitle(proc_name)

    pid_dir = tempfile.gettempdir()
    pid_file = f'{pid_dir}/{proc_name}.pid'
    pid_ok = False
    try:
        with pid.PidFile(proc_name, piddir=pid_dir) as p:
            pid_ok = True

            secure_config = copy.deepcopy(CONFIG)
            secure_config['postgres']['pass'] = '*****'
            secure_config['jwt']['secret'] = '*****'

            DEFAULT_LOGGER.info(f'{SOFTWARE_VERSION} starting, PID: {p.pid}, File: {pid_file}')
            DEFAULT_LOGGER.info(f'Config loaded from {CFG_FILE}:\n{yaml.dump(secure_config, default_flow_style=False)}')

            from pkg.rest import app
            uvicorn.run(app, host=host, port=port, log_config=LOG_CONFIG)
    except:
        if pid_ok:
            raise
        else:
            DEFAULT_LOGGER.critical(f'Something wrong with {pid_file}. Maybe it\'s locked?')
