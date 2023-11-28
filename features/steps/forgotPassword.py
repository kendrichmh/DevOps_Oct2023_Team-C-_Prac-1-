from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


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