

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service("/Users/ashique/projects/python/selenium/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://www.youtube.com/watch?v=hT_nvWreIhg')