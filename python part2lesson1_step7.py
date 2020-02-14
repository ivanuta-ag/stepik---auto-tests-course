from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    print(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    chechbox = browser.find_element_by_id("robotCheckbox")
    chechbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()