# Imports
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Variables 
item_name = 'JOYTOY Warhammer 40K Ultramarines Intercessors V2'

# Common tests
#-------------------------------------------------------------
@given(u'Chrome browser is Launched')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()

@when(u'Open Toyster page')
def openFormyPage(context):
    context.driver.get("https://toyster.sg/")
    context.driver.maximize_window()
    
@then(u'Verify Toyster title is present')
def verifyPageTitle(context):
    title = context.driver.title
    assert title == "TOYSTER Singapore - Online Toys Retailer – Toyster"

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

# Add to cart
#-------------------------------------------------------------
@then(u'Click on category')
def goToCategory(context):
    categoryBtn = context.driver.find_element(By.XPATH,"//a[@title='Action Figures & Collectible']")
    categoryBtn.click()

@then(u'Click on item')
def goToItem(context):
    itemBtn = context.driver.find_element(By.XPATH, f"//div[@class='product-card__name' and text()='{item_name}']")
    itemBtn.click()
    sleep(2)


@then(u'Click on add to cart')
def addItem(context):
    addItemBtn = context.driver.find_element(By.XPATH,"//button[@name='add']")
    addItemBtn.click()
    sleep(8)

@then(u'Click on cart')
def checkItem(context):
    cartBtn = context.driver.find_element(By.XPATH, "//a[@class='site-header__link site-header__cart']")
    cartBtn.click()
    sleep(5)

@then(u'Verify items are in cart')
def verifyCartItemsadded(context):
    item_element = context.driver.find_element(By.XPATH, f"//a[@class='h5 advanced-preorder__Iterated' and contains(text(), '{item_name}')]")
    item_text = item_element.text.strip()
    assert item_text == item_name
    sleep(5)

# Remove from cart
#-------------------------------------------------------------
@then(u'Click on remove')
def removeCartItems(context):
    removeItemsBtn = context.driver.find_element(By.XPATH,"//a[contains(@href, '/cart/change?line=1&quantity=0')]")
    removeItemsBtn.click()
    sleep(5)

@then(u'Verify items are not in cart')
def verifyCartItemsremoved(context):
    cart_empty_message = context.driver.find_element(By.XPATH,"//p[@class='cart--empty-message']")


