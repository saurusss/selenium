from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r'D:\AP\Selenium\chromedriver.exe')
url='https://google.com'
driver.get(url)
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
driver.find_elelments_by_css_selectore('.LC201b')[2].Click()