from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request


@given('I try to get exercise history right')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/exercise/mqwaAIQblczmUExp/history'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify invalid exercise ID')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/exercise/some-invalid-id/history'
    context.response = authorized_behave_request('GET', url)
