from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    button = browser.find_element_by_xpath("//*[@class='btn btn-primary']")
    button.click()

    # Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text

    y = calc(x)

    form = browser.find_element_by_xpath("//*[@class='form-control']")
    form.send_keys(y)

    time.sleep(1)
    button1 = browser.find_element_by_xpath("//*[@class='btn btn-primary']")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
