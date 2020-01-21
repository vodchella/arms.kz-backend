from behave import *
from behave.runner import Context
from tests.behave.utils import behave_request


@given('I try to get exercise list right')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/exercise/list'
    context.response = behave_request('GET', url)
