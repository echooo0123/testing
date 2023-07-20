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



def test_button_delete(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    action_chains = ActionChains(driver)
    delete_boxes = driver.find_element(By.CSS_SELECTOR, '.delete-command')
    action_chains.click(delete_boxes).perform()
    time.sleep(3)
   
    try:
        driver.find_element(By.CSS_SELECTOR, '.command-preview')
        T=False
    except:
         T=True
    assert T

        
    
   