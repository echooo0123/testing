import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

key_list = ["use global", "ls", "test"]



@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()

def send_keys_and_enter(action_chains, keys):
    action_chains.send_keys(keys)
    try:
        action_chains.key_down(Keys.COMMAND)
    except:
        action_chains.key_down(Keys.CONTROL)
    action_chains.key_down(Keys.ENTER)
    action_chains.perform()

def pg_up(action_chains):
    try:
        action_chains.key_down(Keys.COMMAND)
    except:
        action_chains.key_down(Keys.CONTROL)
    action_chains.key_down(Keys.ARROW_UP)
    action_chains.perform()

def pg_down(action_chains):
    try:
        action_chains.key_down(Keys.COMMAND)
    except:
        action_chains.key_down(Keys.CONTROL)
    action_chains.key_down(Keys.ARROW_DOWN)
    action_chains.perform()

    

def test_ctrl_pgdown_shortcut(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)

    # 找到 CodeMirror 元素
    codeMirror = driver.find_element(By.CSS_SELECTOR, ".CodeMirror")

    # 创建动作链对象
    action_chains = ActionChains(driver)

    action_chains.click(codeMirror).perform()
    
    # 输入指令
    for i in range(len(key_list)):
        send_keys_and_enter(action_chains, key_list[i])
        time.sleep(1)
    for i in range(3):
        pg_up(action_chains)
        time.sleep(2)
        
    T = True
    for i in range(2):
        pg_down(action_chains)
        time.sleep(2)
        codeMirror_text = codeMirror.text
        if str(key_list[1+i]) not in codeMirror_text.lower():
            print(f"测试失败: {key_list[1+i]}")
            T = False

    assert T
