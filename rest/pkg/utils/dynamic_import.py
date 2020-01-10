import importlib
import os
from typing import Callable
from glob import glob
from pkg.utils.logger import DEFAULT_LOGGER


def dynamic_import(path: str, module: str, prompt: str, callback: Callable):
    DEFAULT_LOGGER.info(prompt)
    for md in [os.path.basename(x)[:-3] for x in glob(f'{path}/*.py') if x[-11:] != '__init__.py']:
        mdl = importlib.import_module(f'{module}.{md}')
        callback(md, mdl)
