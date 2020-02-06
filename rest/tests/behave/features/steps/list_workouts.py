from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request
from tests.behave.utils.constants import SERVER_API_V1_PATH


@given('I try to get workout list right')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/workout/list'
    context.response = authorized_behave_request('GET', url)
