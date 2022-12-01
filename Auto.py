from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get('http://172.16.100.57:8080/Nexgen23/login.html')
nexgen = driver.switch_to.window
us = nexgen.find_element(By.XPATH, '//*[@id="txtUsuario"]')
us.send_keys('791')

