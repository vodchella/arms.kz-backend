from behave import *
from behave.runner import Context
from tests.behave.utils import behave_request
from tests.behave.utils.constants import SERVER_API_V1_PATH


@given('I try to sign in without token')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/signin/google'
    params = {'some_param': 'some_value'}
    context.response = behave_request('POST', url, params=params)


@given('I try to sign in with invalid Google Auth token')
def step_impl(context: Context):
    url = f'{SERVER_API_V1_PATH}/signin/google'
    params = {'token': 'invalid_token'}
    context.response = behave_request('POST', url, params=params)
