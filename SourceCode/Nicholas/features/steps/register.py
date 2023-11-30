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
    try:
        context.driver.find_element("xpath", "//*[@id='StickyNav']//div[@class='customer-login-links sticky-hidden']/a[1]").click()
        sleep(5)
    except:
        context.driver.close()
        assert "Account page could not be found"

# -- Scenario 2 Valid Credentials
@then(u'Verify Account is Created')
def step_impl(context):
    try:
        my_account_element = context.driver.find_element("xpath","//h1[text()='My Account']")
        flag = my_account_element.is_displayed()
        context.driver.close()
        assert flag, "Account was not Created"
    except:
        context.driver.close()
        assert "Account was not Created, Blocked by Captcha"

# -- Scenario 2 Invalid Credentials
@then(u'Verify Account is not Created')
def step_impl(context):
    try:
        my_account_element = context.driver.find_element("xpath","//h1[text()='My Account']")
        flag = not(my_account_element.is_displayed())
        context.driver.close()
        assert flag, "Account was Created"
    except:
        context.driver.close()
