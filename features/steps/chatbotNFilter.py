from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

#Background
@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()


@when(u'Open Toyster page')
def openToysterPage(context):
    context.driver.get("https://toyster.sg")

#Scenario 1
@then(u'Click Toyster Chatbot')
def clickChatbot(context):
    sleep(3)
    chatbotFrame = context.driver.find_element(By.XPATH,"//iframe[@title='Shopify online store chat']")
    context.driver.switch_to.frame(chatbotFrame)
    chatbotButton = context.driver.find_element(By.TAG_NAME,'button')
    chatbotButton.click()
    context.driver.switch_to.default_content()

@then(u'Click Toyster Chatbot Prompt')
def clickChatbotPrompt(context):
    sleep(3)
    chatbotFrame = context.driver.find_element(By.XPATH,"//iframe[@title='Shopify online store chat']")
    context.driver.switch_to.frame(chatbotFrame)
    chatbotPromptButton = context.driver.find_element(By.XPATH, '//button/p[text()="What is your operating hour?"]')
    chatbotPromptButton.click()
    context.driver.switch_to.default_content()

#Senario 2
@then(u'Select Product')
def goToProductPage(context):
    chatbotButton = context.driver.find_element(By.XPATH,"//a[@title='Action Figures & Collectible']")
    chatbotButton.click()

@then(u'Select Filter Dropdown')
def clickFilter(context):
    filterButton = context.driver.find_element(By.XPATH,"//select[@name='SortTags']")
    filterButton.click()

@then(u'Input multiple "{dropdownOptions}"')
def step_impl(context, dropdownOptions):
    filterDropdown = context.driver.find_element(By.XPATH,'//option[text()="{}"]'.format(dropdownOptions))
    filterDropdown.click()
    
#Close browser
@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()