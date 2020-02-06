from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request
from tests.behave.utils.constants import SERVER_API_V1_PATH


@given('I try to view workout right')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/workout/5WaAWF4KnsoX2eX8/view'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify invalid workout ID')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/workout/some-invalid-id/view'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify nonexistent workout ID')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/workout/nonexistent_id/view'
    context.response = authorized_behave_request('GET', url)
