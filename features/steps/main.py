# Settings
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep


options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Flow
#-------------------------------------------------------------------------
# 1.General Steps
# 2.Register
# 3.Login
# 4.Forget Password
# 5.Search
# 6.Sort
# 7.Filter
# 8.Add to cart
# 9.Remove from cart
# 10.Chatbot
# 11.Customer Review


# General Test -------------------------------------------------------------------------
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

'''
# Login Test -------------------------------------------------------------------------
@when(u'they click the login link')
def customerLoginLink(context):
    customer_login_link = context.driver.find_element(By.ID, 'customer_login_link')
    customer_login_link.click()


@then(u'they should be redirected to the login page')
def loginSuccess(context):
    WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Login')]"))
    )
    LoginText = context.driver.find_element("xpath", "//h1[contains(text(),'Login')]")
    ExpectedText = "Login"
    assert LoginText.text == ExpectedText, "Login not found"
# -- Scenaio 1 Valid Credentials
@when(u'the user enters valid credentials username "{user}" and password "{pwd}"')
def validLogin(context, user, pwd):
    customerEmail = context.driver.find_element(By.ID, "CustomerEmail")
    customerPassword = context.driver.find_element(By.ID, "CustomerPassword")
    customerEmail.send_keys(user)
    customerPassword.send_keys(pwd)

@when(u'clicks the Sign In Button')
def clickSignIn(context):
    customer_SignIn_button = context.driver.find_element(By.XPATH, '//body/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/p[1]/input[1]')
    customer_SignIn_button.click()

@then(u'see My Account Page')
def seeAccPage(context):
    WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'My Account')]"))
    )
    LoginText = context.driver.find_element("xpath", "//h1[contains(text(),'My Account')]")
    ExpectedText = "My Account"
    assert LoginText.text == ExpectedText, "My Account not found"

# -- Scenario 2 Invalid Credentials
@when(u'the user enters invalid credentials username "{user}" and password "{pwd}"')
def invalidLogin(context, user, pwd):
    customerEmail = context.driver.find_element(By.ID, "CustomerEmail")
    customerPassword = context.driver.find_element(By.ID, "CustomerPassword")
    customerEmail.send_keys(user)
    customerPassword.send_keys(pwd)

@then(u'they should see an error message')
def seeError(context):
    WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//body/div[4]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]"))
    )
    LoginText = context.driver.find_element("xpath", "//body/div[4]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]")
    ExpectedText = "Incorrect email or password."
    assert LoginText.text == ExpectedText, "Error Message not Found"
'''
# Register Test -------------------------------------------------------------------------

# Navigate to Register Account page
@when(u'Open Toyster Register Account page')
def step_impl(context):
    context.driver.get("https://toyster.sg/account/register")

# Input fields
@then(u'Input multiple "{firstName}" and "{lastName}" and "{email}" and "{password}"')
def step_impl(context, firstName, lastName, email, password):
    if firstName != 'BLANK':
        context.driver.find_element("id", "FirstName").send_keys(firstName)
    if lastName != 'BLANK':
        context.driver.find_element("id","LastName").send_keys(lastName)
    if email != 'BLANK':
        context.driver.find_element("id","Email").send_keys(email)
    if password != 'BLANK':
        context.driver.find_element("id","CreatePassword").send_keys(password)

@then(u'Click Create')
def step_impl(context): 
    context.driver.find_element("xpath", "//*[@id='create_customer']/p/input[@class='btn']").click()
    sleep(5)


@then(u'Navigate to My Account Page')
def step_impl(context):
    context.driver.find_element("xpath", "//*[@id='StickyNav']//div[@class='customer-login-links sticky-hidden']/a[1]").click()
    sleep(5)

# -- Scenario 2 Valid Credentials
@then(u'Verify Account is Created')
def step_impl(context):
    try:
        my_account_element = context.driver.find_element("xpath","//h1[text()='My Account']")
        assert my_account_element.is_displayed(), "My Account heading is displayed"
    except:
        assert False, "My Account heading is not displayed"

# -- Scenario 2 Invalid Credentials
@then(u'Verify Account is not Created')
def step_impl(context):
    try:
        my_account_element = context.driver.find_element("xpath","//h1[text()='My Account']")
        assert not(my_account_element.is_displayed()), "My Account heading is not displayed"
    except:
        assert True, "My Account heading is displayed"

'''
# Forget Password Test -------------------------------------------------------------------------
@when(u'Click Forgot Password')
def clickForgotPassword(context):
    customer_ForgotPassword_button = context.driver.find_element(By.ID, 'RecoverPassword')
    customer_ForgotPassword_button.click()

@when(u'Enter email "{email}" to reset Password')
def enterForgotPasswordEmail(context,email):
    forgotPasswordEmail = context.driver.find_element(By.ID, "RecoverEmail")
    forgotPasswordEmail.send_keys(email)

@when(u'Click Submit')
def clickSubmit(context):
    ForgotPasswordSubmit_button = context.driver.find_element(By.XPATH, '//body/div[3]/main[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/form[1]/p[1]/input[1]')
    ForgotPasswordSubmit_button.click()

@then(u'see We\'ve sent you an email with a link to update your password')
def seeConfirmation(context):
    WebDriverWait(context.driver, 10).until(
    EC.visibility_of_element_located((By.ID, "ResetSuccess"))
    )
    ConfirmationText = context.driver.find_element(By.ID, "ResetSuccess")
    ExpectedText = "We've sent you an email with a link to update your password."
    assert ConfirmationText.text == ExpectedText, "Error Message not Found"

# Search Test -------------------------------------------------------------------------
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

# Sort Test -------------------------------------------------------------------------
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

# Filter Test -------------------------------------------------------------------------
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

# Add to Cart Test -------------------------------------------------------------------------
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

# Remove from Cart Test -------------------------------------------------------------------------
@then(u'Click on remove')
def removeCartItems(context):
    removeItemsBtn = context.driver.find_element(By.XPATH,"//a[contains(@href, '/cart/change?line=1&quantity=0')]")
    removeItemsBtn.click()
    sleep(5)

@then(u'Verify items are not in cart')
def verifyCartItemsremoved(context):
    cart_empty_message = context.driver.find_element(By.XPATH,"//p[@class='cart--empty-message']")

# Chatbot Test -------------------------------------------------------------------------
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
'''