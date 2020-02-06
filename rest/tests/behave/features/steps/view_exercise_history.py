from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request
from tests.behave.utils.constants import SERVER_API_V1_PATH


@given('I try to get exercise history right')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/exercise/mqwaAIQblczmUExp/history'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify invalid exercise ID')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/exercise/some-invalid-id/history'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify nonexistent exercise ID')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/exercise/nonexistent_id/history'
    context.response = authorized_behave_request('GET', url)
