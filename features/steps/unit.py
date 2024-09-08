from behave import given, when, then
from unittest.mock import Mock

mock_object = None
utility_result = None


@given("a mock object is created")
def step_impl(context):
    global mock_object
    mock_object = Mock(return_value="expected result")


@when("the mock object is called")
def step_impl(context):
    context.result = mock_object()


@then("it should return the expected result")
def step_impl(context):
    assert context.result == "expected result"


@given("a utility function is available")
def step_impl(context):
    def utility_function():
        return "correct output"

    context.utility_function = utility_function


@when("I call the utility function")
def step_impl(context):
    global utility_result
    utility_result = context.utility_function()


@then("it should return the correct output")
def step_impl(context):
    assert utility_result == "correct output"
