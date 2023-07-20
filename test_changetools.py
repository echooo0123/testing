import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()



def test_change_tools(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    
    # 创建动作链对象
    action_chains = ActionChains(driver)
    change_boxes = driver.find_element(By.CSS_SELECTOR, '.btn')
    action_chains.click(change_boxes).perform()
    
