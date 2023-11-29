from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


#General Test

@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(options=options)

@when(u'Open Toyster page')
def openToysterPage(context):
    context.driver.get("https://toyster.sg")

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()