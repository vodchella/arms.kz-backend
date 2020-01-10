import os
import sys
from pkg.utils.errors import get_raised_error


def write_stderr(line: str):
    sys.stderr.write(line)
    sys.stderr.flush()


def write_stdout(line: str):
    sys.stdout.write(line)
    sys.stdout.flush()


def panic(msg: str = None, show_original_error: bool = False):
    if not msg:
        msg = get_raised_error()
    elif show_original_error:
        write_stderr(get_raised_error())
    write_stderr(f'{msg}\n')
    # noinspection PyProtectedMember
    os._exit(1)
