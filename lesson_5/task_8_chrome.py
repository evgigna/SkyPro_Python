# Задание 8. Форма авторизации

# Напишите скрипт.
# Шаги:
# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith.
# В поле password введите значение SuperSecretPassword!.
# Нажмите кнопку Login.


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# переход на урл http://the-internet.herokuapp.com/login.
driver.get("http://the-internet.herokuapp.com/login")

try:   
    # Ожидаем загрузки страницы
    wait = WebDriverWait(driver, 10)
    
    input_username = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#username")))

    input_username.send_keys('tomsmith')
    print('Имя пользователя введено')
    sleep(2)

    input_password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#password")))

    input_password.send_keys('SuperSecretPassword!')
    print('Пароль введен')
    sleep(2)

    login_button = driver.find_element(By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')
    login_button.click()
    print('Клик на кнопку выполнен')
    sleep(2)
   
except Exception as ex:
    print(f"Произошла ошибка: {ex}")
    
finally:
    driver.quit()