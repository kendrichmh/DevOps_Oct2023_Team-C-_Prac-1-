from common_steps import *
from time import sleep

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
    sleep(5)

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
