from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'Open Toyster page')
def openToysterPage(context):
    context.driver.get("https://toyster.sg")