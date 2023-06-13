from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1. Зайти на главную страницу
# 2. Открыть страницу login
# 3. Заполнить поле email
# 4. Заполнить поле password
# 5. Нажать на кнопку start

URL = 'https://berpress.github.io/react-shop/'
LOGIN = 'test@test.com'
PASSWORD = 'Password1'

#1
driver.get(URL)
#2
login_page_button = driver.find_element(By.ID, 'login-link')
login_page_button.click()

#3, 4
input_login = driver.find_element(By.ID, 'name')
input_password = driver.find_element(By.ID, 'password')
input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)

# 5
register_button = driver.find_element(By.ID, 'register')
register_button.click()

