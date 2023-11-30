from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


#General Test

@given('Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(options=options)

@when('Open Toyster page')
def openToysterPage(context):
    context.driver.get("https://toyster.sg")

@then('Close Chrome browser')
def closeBrowser(context):
    try:
        context.driver.close()
    except:
        pass