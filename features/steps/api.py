import requests
from behave import given, when, then
from utils.apicontext import handle_context

BASE_URL = "https://www.google.com"  # Replace with the actual API URL
response = None

@given("I make a request to the free API")
def step_make_request(context):
    global response
    handle_context(context)
    response = requests.get(f"{BASE_URL}/")  
    print(response.status_code)

@when("I receive the response")
def step_receive_response(context):
    handle_context(context)
    assert response is not None

@then("the response status should be 200")
def step_check_status(context):
    handle_context(context)
    assert response.status_code == 200
