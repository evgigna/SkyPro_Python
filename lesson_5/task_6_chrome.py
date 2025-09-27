# Задание 6. Модальное окно

# Напишите скрипт.
# Шаги:
# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
# В модальном окне нажмите на кнопку Сlose.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# переход на урл http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:
    wait = WebDriverWait(driver, 10)

    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
    sleep(2)

    close_button.click()
    print("Клик на кнопку CLOSE успешный!")
    sleep(2)
        
except Exception:
    print(f"Ошибка при поиске кнопки!")
    sleep(5)

finally:
    driver.quit()