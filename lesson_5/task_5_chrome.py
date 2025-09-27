# Задание 5. Клик по кнопке с CSS-классом

# Напишите скрипт.
# Шаги:
# Откройте страницу http://uitestingplayground.com/classattr.
# Кликните на СИНЮЮ кнопку.
# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# переход на урл http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")

try:
    search_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary[type='button']")
    
    try:
        search_button.click()
        print("Клик выполнен успешно!")      
        sleep(2)    
    except (ElementNotInteractableException, ElementClickInterceptedException):
        print(f"Не удалось кликнуть на кнопку")
        
except Exception as e:
    print(f"Ошибка при поиске кнопки")

finally:
    driver.quit()