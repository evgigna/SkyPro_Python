# Задание 3. Клик по кнопке

# Напишите скрипт.
# Шаги:
# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку Add Element
# Соберите со страницы список кнопок Delete
# Выведите на экран размер списка.


from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# переход на урл http://the-internet.herokuapp.com/add_remove_elements/.
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

search_button = driver.find_element(By.CSS_SELECTOR, "#content > div > button")

# клик на кнопку Add Element 5 раз
for i in range(5):
    search_button.click()

# формирование списка кнопок Delete
buttons = driver.find_elements(By.CSS_SELECTOR, "#elements > button")

# вывод на экран размера списка
print("Размер списка: count = ", len(buttons))

sleep(5)

driver.quit()