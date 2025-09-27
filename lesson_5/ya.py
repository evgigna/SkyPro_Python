from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

sleep(5)

driver.get("https://ya.ru/")

driver.maximize_window()

sleep(5)

driver.get("https://vk.com/")

driver.fullscreen_window()

driver.save_screenshot('./vk.jpeg')

sleep(5)