from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('e:\AP\Selenium\chromedriver.exe')
url = 'https://google.com'
driver.get(url)
driver.maximize_window()   
action = ActionChains(driver)

driver.find_element_by_css_selector('#gb_70').click()  # id / class 모두 찾을수 있음(css-selector)- 로그인버튼 찾아서 클릭
# action.send_keys('saurusss').perform()
# action.reset_actions()

driver.find_element_by_css_selector('.BHzsHc').click()

driver.find_element_by_css_selector('.whsOnd zHQkBf').send_keys('saurusss')
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
driver.find_element_by_css_selector('.whsOnd zHQkBf').send_keys('didakf12g,')
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
driver.get('https://mail.google.com/mail/u/0/?ogbl#inbox')
time.sleep(2)

driver.find_element_by_css_selector('.T-I.T-I-KE.L3').click()

send_button = driver.find_element_by_css_selector('.gU.Up')

(
action.send_keys('saurusss@gmail.com').pause(2).key_down(Keys.TAB).key_down(Keys.TAB)
    .send_keys('제목입니다.').pause(2).key_down(Keys.TAB)
    .send_keys('abcde.').pause().key_down(Keys.ENTER)
    .key_down(Keys.SHIFT).send_keys('abcde').key_up(Keys.SHIFT)
    .move_to_element(send-button).click()
    .perform()
)

