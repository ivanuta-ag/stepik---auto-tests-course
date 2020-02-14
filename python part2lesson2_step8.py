from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
import os

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

# автоматом создать текстовый файл test.txt
with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file

try:
    link = "http://suninjuly.github.io/file_input.html"
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    input1 = browser.find_element_by_xpath("//body/div/form/div/input[@name='firstname']")
    input1.send_keys('Vova')

    input2 = browser.find_element_by_xpath("//body/div/form/div/input[@name='lastname']")
    input2.send_keys("Ivanov")

    input3 = browser.find_element_by_xpath("//body/div/form/div/input[@name='email']")
    input3.send_keys("1@gmail.com")

    attach = browser.find_element_by_xpath("//body/div/form/input[@id='file']")
    # attach = browser.find_element_by_id('file')
    attach.send_keys(file_path)

    print(file_path)

    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()

finally:
    time.sleep(20)
    browser.quit()
