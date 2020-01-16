from behave import *
from behave.runner import Context


@then('I will get "{http_error_code}" http error')
def step_impl(context: Context, http_error_code: str):
    assert context.response.status_code == int(http_error_code)


@then('I will get "{http_error_code}" http error with "{app_error_code}" application error')
def step_impl(context: Context, http_error_code: str, app_error_code: str):
    json = context.response.json()
    assert json['error']['code'] == int(app_error_code)
    assert context.response.status_code == int(http_error_code)


@then('I will get "{http_error_code}" http error or "{http_error_code2}" http error with "{app_error_code}" app error')
def step_impl(context: Context, http_error_code: str, http_error_code2: str, app_error_code: str):
    json = context.response.json()
    assert (context.response.status_code == int(http_error_code)) or \
        (context.response.status_code == int(http_error_code2) and json['error']['code'] == int(app_error_code))


@then('I will get Ok http status')
def step_impl(context: Context):
    assert context.response.status_code == 200


@then('I will get Ok http status and "{result}" result')
def step_impl(context: Context, result: str):
    json = context.response.json()
    assert json['result'] == result
    assert context.response.status_code == 200
