from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.implicitly_wait(10)
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


def open_login_page(driver):
    element_click(driver, 'login-link')


def login(driver, name, password):
    element_send_keys(driver, 'name', name)
    element_send_keys(driver, 'password', password)
    element_click(driver, 'register')



driver = get_driver()
open_page(driver, URL)
open_login_page(driver)
login(driver=driver, name=LOGIN, password=PASSWORD)

driver.quit()