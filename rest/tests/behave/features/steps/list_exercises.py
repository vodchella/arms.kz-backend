from behave import *
from behave.runner import Context
from tests.behave.utils import behave_request


@given('I try to do it right')
def step_impl(context: Context):
    url = 'http://localhost:8517/v1/exercise/list'
    context.response = behave_request('GET', url)


@then('I will get Ok http status')
def step_impl(context: Context):
    assert context.response.status_code == 200
