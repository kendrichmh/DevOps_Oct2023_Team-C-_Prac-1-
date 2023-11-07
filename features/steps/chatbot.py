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


@then(u'Click Toyster Chatbot')
def verifyChatbot(context):
    sleep(3)
    chatbotFrame = context.driver.find_element(By.XPATH,"//iframe[@title='Shopify online store chat']")
    context.driver.switch_to.frame(chatbotFrame)
    chatbotButton = context.driver.find_element(By.TAG_NAME,'button')
    chatbotButton.click()

@then(u'Select Product')
def goToProductPage(context):
    chatbotButton = context.driver.find_element(By.XPATH,"//a[@title='Action Figures & Collectible']")
    chatbotButton.click()

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()