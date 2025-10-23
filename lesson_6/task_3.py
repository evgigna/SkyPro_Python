# Задание 3. Дождаться картинки
# Напишите скрипт.
# Шаги:
# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src у 3-й картинки.
# Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    waiter = WebDriverWait(driver, 30)

    img_1 = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#compass")))
    img_2 = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#calendar")))
    img_3 = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))
    img_4 = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))

    print("src = ", driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src"))

finally:
    driver.quit()