from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#Searching Test

@then(u'Input Toyname "{toyName}"')
def inputToyName(context,toyName):
    context.driver.find_element("id", "SiteNavSearch").send_keys(toyName)
    sleep(5)
    

@then(u'Select Search')
def ClickSearch(context):
    searchbar = context.driver.find_element(By.XPATH,"//*[@id='SiteNavSearchCart']/form/button")
    searchbar.click()
    sleep(2)

@then(u'View Product')
def ViewProduct(context):
    viewToy = context.driver.find_element(By.XPATH,"//*[@id='MainContent']/div/div[1]/div[2]/a/div[1]")
    viewToy.click()
    sleep(2)


