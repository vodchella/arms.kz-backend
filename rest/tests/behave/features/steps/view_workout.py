from behave import *
from behave.runner import Context
from tests.behave.utils import behave_request


@given('I try to view workout right')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/workout/some_id/view'
    context.response = behave_request('GET', url)


@given('I try to specify invalid workout ID')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/workout/some-invalid-id/view'
    context.response = behave_request('GET', url)
