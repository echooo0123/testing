import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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

expected_state=[False,True,False]

def test_search_graph(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    
    interactive = driver.find_element(By.CSS_SELECTOR, ".graph-selector")
    action_chains = ActionChains(driver)
    action_chains.click(interactive).perform()

    time.sleep(5)
    checkbox = driver.find_element(By.XPATH, '//*[@id="bui18val-1"]')
    checkbox.click()
    time.sleep(5)
    whole = driver.find_elements(By.XPATH, '//*[@id="bui18val-0"] | //*[@id="bui18val-1"] | //*[@id="bui18val-2"]')
    T=True
   
    count=0
    for checkbox in whole:
        checkbox_state = checkbox.is_selected()
        if checkbox_state == expected_state[count]:
           count+=1
        else:
            T=False
    assert T
        
    



