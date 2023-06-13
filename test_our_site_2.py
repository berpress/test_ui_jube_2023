from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# 1. Зайти на главную страницу
# 2. Открыть страницу login
# 3. Заполнить поле email
# 4. Заполнить поле password
# 5. Нажать на кнопку start

URL = 'https://berpress.github.io/react-shop/'
LOGIN = 'test@test.com'
PASSWORD = 'Password1'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def open_page(driver, url):
    driver.get(url)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)

def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)


#1
driver = get_driver()
open_page(driver, URL)
#2
element_click(driver, 'login-link')
#3, 4
element_send_keys(driver, 'name', LOGIN)
element_send_keys(driver, 'password', PASSWORD)
# 5
element_click(driver, 'register')


