import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()



def test_upload(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    action_chains = ActionChains(driver)
    button_boxes = driver.find_elements(By.CSS_SELECTOR, 'button[data-baseweb="button"]')[2]
    action_chains.click(button_boxes).perform()
    #time.sleep(5)
    button_boxes=driver.find_elements(By.CSS_SELECTOR, 'button[data-baseweb="button"]')[3]
    action_chains.click(button_boxes).perform()
    time.sleep(5)
    driver.find_element(By.NAME,"gsql-upload").send_keys("C:\\Users\\jingyiYang\\Desktop\\work\\testing_input.gsql")
    action_chains.key_down(Keys.ENTER)
    codeMirror = driver.find_element(By.CSS_SELECTOR, ".CodeMirror")
    codeMirror_text = codeMirror.text
    assert codeMirror_text =="ls" 
    
    
