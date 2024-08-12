from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *
from time import sleep

def test_form_fillin(chrome_browser):
    chrome_browser.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys('Иван')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="last-name"]').send_keys('Петров')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys('Ленина, 55-3')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys('test@skypro.com')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys('+7985899998787')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys('')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys('Москва')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys('Россия')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys('QA')
    chrome_browser.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys('SkyPro')

    chrome_browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

    red_color = chrome_browser.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
    print(red_color)
    assert red_color == 'rgba(248, 215, 218, 1)'
    print("Assertion passed, background color is red.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
    print(green_color)
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = chrome_browser.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")