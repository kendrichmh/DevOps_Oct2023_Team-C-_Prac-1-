from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from time import sleep

#Sorting  Test

@then(u'MainMenu Sorting')
def MainSort(context):
    dropdown = context.driver.find_element(By.XPATH,"//*[@id='SiteNavCompressed']")
    dropdown.click()    
    sleep(2)


@then(u'Categories Sorting')
def BlasterSort(context):
    SortByCategories= context.driver.find_element(By.XPATH,"//*[@id='NavDrawer']/div/ul/li[3]/div[1]")
    SortByCategories.click()

@then(u'SortBY')
def SortBy(context):
    Sort =  context.driver.find_element(By.XPATH,"//*[@id='SortBy']") 
    drop=Select(Sort)
    # select by visible text
    drop.select_by_visible_text("Date, new to old")
