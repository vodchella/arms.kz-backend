from behave import *
from behave.runner import Context
from tests.behave.utils import behave_request


@given('I try to sign in without token')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/signin/google'
    params = {'some_param': 'some_value'}
    context.response = behave_request('POST', url, params=params)


@given('I try to sign in with invalid Google Auth token')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/signin/google'
    params = {'token': 'invalid_token'}
    context.response = behave_request('POST', url, params=params)
