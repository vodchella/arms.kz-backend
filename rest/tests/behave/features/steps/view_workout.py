from behave import *
from behave.runner import Context
from tests.behave.utils import authorized_behave_request


@given('I try to view workout right')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/workout/5WaAWF4KnsoX2eX8/view'
    context.response = authorized_behave_request('GET', url)


@given('I try to specify invalid workout ID')
def step_impl(context: Context):
    url = 'http://localhost:8517/api/v1/workout/some-invalid-id/view'
    context.response = authorized_behave_request('GET', url)
