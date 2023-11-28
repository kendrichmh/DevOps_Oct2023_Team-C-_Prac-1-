from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



#Background
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
###########################################################################################
#Scenaio 1 Valid Credentials
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
##############################################################################################
#Scenario 2 Invalid Credentials
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