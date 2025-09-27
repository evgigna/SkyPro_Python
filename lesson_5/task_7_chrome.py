# Задание 7. Поле ввода

# Напишите скрипт.
# Шаги:
# Откройте страницу http://the-internet.herokuapp.com/inputs.
# Введите в поле текст 1000.
# Очистите это поле (метод clear).
# Введите в это же поле текст 999.


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# переход на урл http://the-internet.herokuapp.com/inputs.
driver.get("http://the-internet.herokuapp.com/inputs")

try:   
    # Ожидаем загрузки страницы
    wait = WebDriverWait(driver, 10)
    
    input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='number']")))
    
    input_field.send_keys("1000")
    print(f'Число 1000 введено')
    sleep(1)
    
    input_field.clear()
    print(f'Поле ввода очищено')
    sleep(1)
    
    input_field.send_keys("999")
    print(f'Число 999 введено')
    sleep(2)


   
except Exception as ex:
    print(f"Произошла ошибка: {ex}")
    
finally:
    driver.quit()