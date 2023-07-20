import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()
# def test_button_duplicate(driver):
#     driver.get('http://34.28.121.9:14240/gsql/')

#     # 使用WebDriverWait等待按钮加载完成并且可见
#     wait = WebDriverWait(driver, 10)
#     duplicate_boxes = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.command-copy')))

#     # 执行鼠标移动操作
#     action_chains = ActionChains(driver)
#     action_chains.move_to_element(duplicate_boxes).perform()

#     # 可以继续执行其他操作，或者省略time.sleep()

#     # 等待一段时间，方便观察鼠标移动效果
#     time.sleep(5)
def test_button_duplicate(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    action_chains = ActionChains(driver)
    duplicate_boxes = driver.find_element(By.CSS_SELECTOR, '.command-copy')
    #action_chains.move_to_element(duplicate_boxes).perform()
    time.sleep(5)
    action_chains.click(duplicate_boxes).perform()
   
    #找到 CodeMirror 元素
    codeMirror = driver.find_element(By.CSS_SELECTOR, ".CodeMirror")
    
    assert codeMirror.text==":help"
