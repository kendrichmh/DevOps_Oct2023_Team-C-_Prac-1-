from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open Toyster page')
def openToysterPage(context):
    context.driver.get("https://toyster.sg")


@then(u'Verify Toyster Title is present')
def verifyPageTitle(context):
    title = context.driver.title
    assert title == "TOYSTER Singapore - Online Toys Retailer – Toyster"

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()



@then(u'Input Toyname "{toyName}"')
def inputToyName(context,toyName):
    context.driver.find_element("id", "SiteNavSearch").send_keys(toyName)
    sleep(5)

@then(u'Select Search')
def ClickSearch(context):
    searchbar = context.driver.find_element(By.XPATH,"//*[@id='SiteNavSearchCart']/form/button")
    searchbar.click()
    sleep(5)

@then(u'View Product')
def ViewProduct(context):
    viewToy = context.driver.find_element(By.XPATH,"//*[@id='MainContent']/div/div[1]/div[2]/a/div[1]")
    viewToy.click()
    sleep(5)
