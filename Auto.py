from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://172.16.100.57:8080/Nexgen23/login.html')
driver.switch_to.window
driver.find_element(By.XPATH, '//*[@id="txtUsuario"]')
driver.send_keys('791')

