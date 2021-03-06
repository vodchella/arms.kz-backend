from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request
from tests.behave.utils.constants import SERVER_API_V1_PATH


@given('I try to view exercise right')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/exercise/3j7VPlHrsw5vf9YR/view'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify invalid exercise ID')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/exercise/some-invalid-id/view'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify nonexistent exercise ID')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/exercise/nonexistent_id/view'
    context.response = authorized_behave_request('GET', url)
