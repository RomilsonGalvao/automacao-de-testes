from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('http://172.16.100.57:8080/Nexgen23/')
nexgen = driver.current_window_handle
driver.find_element(By.ID, 'txtUsuario')
sleep(5)
for handle in driver.window_handles: 
    if handle != nexgen: 
        login_page = handle