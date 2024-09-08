from behave import fixture, use_fixture
from selenium import webdriver
from utils.logging import configure_logging, logging

configure_logging() 

@fixture
def browser_chrome(context):
    logging.info("Starting Chrome browser") 
    context.browser = (
        webdriver.Chrome()
    )
    yield context.browser
    logging.info("Quitting Chrome browser")  
    context.browser.quit()

def before_all(context):
    logging.info("Setting up the test environment")  
    use_fixture(browser_chrome, context)


def after_all(context):
    logging.info("Finishing up test run")  
    pass