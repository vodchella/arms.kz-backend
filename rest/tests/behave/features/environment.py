from behave.runner import Context
from tests.behave.utils import checked_behave_request
from tests.behave.utils.constants import SERVER_API_PATH


# noinspection PyUnusedLocal
def before_all(context: Context):
    try:
        json = checked_behave_request('GET', SERVER_API_PATH)
    except:
        raise Exception('Can\'t connect to server')
    if 'software' not in json:
        raise Exception('Invalid response format')
    if not json['software'].startswith('Arms.kz REST server v'):
        raise Exception('Invalid software version')
