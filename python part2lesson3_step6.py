from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    button = browser.find_element_by_xpath("//*[@class='trollface btn btn-primary']")
    button.click()

    current_window = browser.current_window_handle
    print(current_window)

    # переключаемся на вторую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    print(new_window)

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text

    y = calc(x)

    input = browser.find_element_by_xpath("//*[@class='form-control']")
    input.send_keys(y)

    time.sleep(1)
    button1 = browser.find_element_by_xpath("//*[@class='btn btn-primary']")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
