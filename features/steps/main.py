from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
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


@then(u'Verify Toyster title is present')
def verifyPageTitle(context):
    title = context.driver.title
    assert title == "TOYSTER Singapore - Online Toys Retailer – Toyster"

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

# Search Test
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

# Sort Test

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

# Filter Test
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

# Add to Cart Test
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

# Remove from Cart Test
@then(u'Click on remove')
def removeCartItems(context):
    removeItemsBtn = context.driver.find_element(By.XPATH,"//a[contains(@href, '/cart/change?line=1&quantity=0')]")
    removeItemsBtn.click()
    sleep(5)

@then(u'Verify items are not in cart')
def verifyCartItemsremoved(context):
    cart_empty_message = context.driver.find_element(By.XPATH,"//p[@class='cart--empty-message']")

# Chatbot Test
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
