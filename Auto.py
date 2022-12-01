from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://172.16.100.57:8080/Nexgen23/login.html')
nexgen = driver.switch_to.window
us = nexgen.find_element(By.CSS_SELECTOR, '#txtUsuario')
us.send_keys('791')

