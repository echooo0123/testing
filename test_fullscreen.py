import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

# 模拟按下Fn键

@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    #driver.quit()

def test_full_screen(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)

    # 找到 CodeMirror 元素
    codeMirror = driver.find_element(By.CSS_SELECTOR, ".CodeMirror")

    # 创建动作链对象
    action_chains = ActionChains(driver)

    action_chains.click(codeMirror).perform()

    
    pyautogui.keyDown('fn')
    pyautogui.press('f11')
   
    time.sleep(5)
    action_chains.perform()
    assert driver.find_element(By.CSS_SELECTOR,".editor-fullscreen")

