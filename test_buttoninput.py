import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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



def test_button_input(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    # 找到 CodeMirror 元素
    codeMirror = driver.find_element(By.CSS_SELECTOR, ".CodeMirror")
    # 查找所有的 history-item 类元素
    history_elements = driver.find_elements(By.CLASS_NAME, 'history-item')
    # 计算 history-item 类元素的数量
    initial_history_length = len(history_elements)

    # 创建动作链对象
    action_chains = ActionChains(driver)

    # 点击 CodeMirror 元素
    action_chains.click(codeMirror).perform()


    # 在输入框中键入文本
    action_chains.send_keys("use global").perform()
    time.sleep(2)
    button_boxes = driver.find_element(By.CSS_SELECTOR, 'button[data-baseweb="button"]')
    action_chains.click(button_boxes).perform()
    
    T=True
    
    
    # 查找更新后的 history-item 类元素
    updated_history_elements = driver.find_elements(By.CLASS_NAME, 'history-item')
    

    # 计算更新后的 history-item 类元素的数量
    updated_history_length = len(updated_history_elements)
    element=driver.find_elements(By.CLASS_NAME, 'command-preview')
    T=True
    if element[1].text=="use global" and updated_history_length==initial_history_length+1:
        pass
    else:
        T=False
    assert T