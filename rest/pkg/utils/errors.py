import sys
import traceback


def get_raised_error(full: bool = False):
    info = sys.exc_info()
    if info[0] is None and info[1] is None and info[2] is None:
        return
    e = traceback.format_exception(*info)
    if full:
        return '\n'.join(e)
    else:
        return (e[-1:][0]).strip('\n')
