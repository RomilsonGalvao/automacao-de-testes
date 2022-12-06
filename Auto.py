import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get_window_size('http://172.16.100.57:8080/Nexgen23/')


time.sleep(5)
WebDriverWait(driver, 15)
usu = driver.find_element(By.XPATH, '//*[@id="txtUsuario"]')
login = usu.send_keys('791')







