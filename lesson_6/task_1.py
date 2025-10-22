# Задание 1. Нажатие на кнопку
# Напишите скрипт.
# Шаги:
# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль (”Data loaded with AJAX get request.”).

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get("http://www.uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")

print(content.find_element(By.CSS_SELECTOR, "p.bg-success").text)

driver.quit()

