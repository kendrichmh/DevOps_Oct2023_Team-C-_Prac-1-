"""
Product - //div[@class='grid__item small--one-half medium-up--one-fifth'][1]/a[@class='product-card advanced-preorder__Iterated']/div[@class='product-card__info']/div[@class='product-card__name']
Review - //a[@class='spr-summary-actions-newreview']
Name - //input[contains(@class, 'spr-form-input-text') and @placeholder='Enter your name']
Email - //input[contains(@class, 'spr-form-input-email') and @placeholder='john.smith@example.com']
Stars - //*/fieldset[2]/div[1]/div/a[5]
Title - //input[contains(@class, 'spr-form-input-text') and @placeholder='Give your review a title']
Comments - //textarea[contains(@class, 'spr-form-input')]
Submit Button - //input[@class='spr-button spr-button-primary button button-primary btn btn-primary']
Success Message - //div[@id='shopify-product-reviews']//div[@class='spr-content']/div[contains(@class, 'spr-form-message-success')]
Error Message - //div[@class='spr-form-message spr-form-message-error']
"""

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('Open Toyster Toysterific Sale page')
def step_impl_open_page(context):
    context.driver.get("https://toyster.sg/collections/toysterific-sale")

@then('Click on Product "<productNumber>"')
def step_impl_click_first_product(context, productNumber):
    context.driver.find_element("xpath", f"//div[@class='grid__item small--one-half medium-up--one-fifth'][{productNumber}]/a[@class='product-card advanced-preorder__Iterated']/div[@class='product-card__info']/div[@class='product-card__name']").click()

@then('Click on Write a review')
def step_impl_click_write_review(context):
    context.driver.find_element("xpath", "//a[@class='spr-summary-actions-newreview']").click()

@then('Input "{name}", "{email}", "{rating}", "{title}" and "{body}"')
def step_impl_input_review_details(context, name, email, rating, title, body):
    if name != 'BLANK':
        context.driver.find_element("xpath", "//input[contains(@class, 'spr-form-input-text') and @placeholder='Enter your name']").send_keys(name)
    if email != 'BLANK':
        context.driver.find_element("xpath", "//input[contains(@class, 'spr-form-input-email') and @placeholder='john.smith@example.com']").send_keys(email)
    if rating != 'BLANK':
        context.driver.find_element("xpath", "//*/fieldset[2]/div[1]/div/a[{}]".format(rating)).click()
    if title != 'BLANK':
        context.driver.find_element("xpath", "//input[contains(@class, 'spr-form-input-text') and @placeholder='Give your review a title']").send_keys(title)
    if body != 'BLANK':
        context.driver.find_element("xpath", "//textarea[contains(@class, 'spr-form-input')]").send_keys(body)


@then('Click Submit Review')
def step_impl_submit_review(context):
    context.driver.find_element("xpath", "//input[@class='spr-button spr-button-primary button button-primary btn btn-primary']").click()

@then('Verify Review Sucess Message')
def step_impl_verify_success_message(context):
    try:
        success_element = context.driver.find_element("xpath","//div[@id='shopify-product-reviews']//div[@class='spr-content']/div[contains(@class, 'spr-form-message-success')]")
        assert success_element.is_displayed(), "Review Posted Successfully"
    except:
        assert False, "Review was not posted"

@then('Verify Review Error Message')
def step_impl_verify_success_message(context):
    try:
        error_element = context.driver.find_element("xpath","//div[@class='spr-form-message spr-form-message-error']")
        assert not(error_element.is_displayed()), "Review was not posted"
    except:
        assert False, "There was no error message"

# @then('Close browser')

