from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request


@given('I try to get workout list right')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/workout/list'
    context.response = authorized_behave_request('GET', url)
