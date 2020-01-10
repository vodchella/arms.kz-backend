import copy
import sys
import yaml
import uvicorn
from fastapi import FastAPI
from pkg.config import CONFIG, CFG_FILE
from pkg.constants.version import SOFTWARE_VERSION
from pkg.utils.console import panic
from pkg.utils.logger import DEFAULT_LOGGER, LOG_CONFIG

app = FastAPI()


@app.get('/')
async def root():
    return {
        'software': SOFTWARE_VERSION,
    }


if __name__ == "__main__":
    if sys.version_info < (3, 8):
        panic('We need minimum Python version 3.8 to run. Current version: %s.%s.%s' % sys.version_info[:3])

    secure_config = copy.deepcopy(CONFIG)
    secure_config['postgres']['pass'] = '*****'

    DEFAULT_LOGGER.info(f'Config loaded from {CFG_FILE}:\n{yaml.dump(secure_config, default_flow_style=False)}')
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=LOG_CONFIG)
