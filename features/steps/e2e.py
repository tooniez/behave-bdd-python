from behave import given, when, then


@given("I open the Google webpage")
def step_open_google_webpage(context):
    context.browser.get("https://www.google.com")


@when('I search for "{query}"')
def step_search(context, query):
    search_box = context.browser.find_element("name", "q")
    search_box.send_keys(query)
    search_box.submit()


@then('I should see results for "{query}"')
def step_see_results(context, query):
    results_element = context.browser.find_element("css selector", "head > title")
    assert query in results_element.get_attribute("innerText")
