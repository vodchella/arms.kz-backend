from behave.runner import Context
from tests.behave.utils import checked_behave_request


# noinspection PyUnusedLocal
def before_all(context: Context):
    try:
        json = checked_behave_request('GET', 'http://localhost:8517/')
    except:
        raise Exception('Can\'t connect to server')
    if 'software' not in json:
        raise Exception('Invalid response format')
    if not json['software'].startswith('ArmGym REST server v'):
        raise Exception('Invalid software version')
