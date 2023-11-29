from common_steps import then, sleep, By

# Navigate to Register Account page
@then('Navigate to Register Account page')
def step_impl(context):
    context.driver.get("https://toyster.sg/account/register")

@then('Input multiple "{firstName}", "{lastName}", "{email}" and "{password}"')
def step_impl(context, firstName, lastName, email, password):
    context.driver.find_element("id","FirstName").send_keys(firstName)
    context.driver.find_element("id","LastName").send_keys(lastName)
    context.driver.find_element("id","Email").send_keys(email)
    context.driver.find_element("id","CreatePassword").send_keys(password)
    context.driver.driver.find_element_by_class_name("btn").click()
    sleep(5)


@then('Navigate to My Account Page')
def step_impl(context):
    context.driver.get("https://toyster.sg/account")


@then('Verify Account is Created')
def step_impl(context):
    try:
        # Check for the presence of the <h1>My Account</h1> element by its XPath
        my_account_element = context.driver.find_element_by_xpath("//h1[text()='My Account']")
        assert my_account_element.is_displayed(), "My Account heading is displayed"
    except:
        assert False, "My Account heading is not displayed"

@then('Verify Account is not Created')
def step_impl(context):
    try:
        # Check for the presence of the <h1>My Account</h1> element by its XPath
        my_account_element = context.driver.find_element_by_xpath("//h1[text()='My Account']")
        assert not(my_account_element.is_displayed()), "My Account heading is not displayed"
    except:
        assert True, "My Account heading is displayed"


# @then('Close browser')
