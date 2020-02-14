from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "100")
    )

    button = browser.find_element_by_xpath("//*[@id='book']")
    button.click()

    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text

    y = calc(x)

    input = browser.find_element_by_xpath("//*[@id='answer']")
    input.send_keys(y)

    submit = browser.find_element_by_xpath("//*[@id='solve']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    browser.switch_to.alert