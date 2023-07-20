import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

key_list = ["use global", "ls"]

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


def test_history_display(driver):
    T=True
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)

    # 找到 CodeMirror 元素
    codeMirror = driver.find_element(By.CSS_SELECTOR, ".CodeMirror")

    # 创建动作链对象
    action_chains = ActionChains(driver)

    action_chains.click(codeMirror).perform()
    test_list=["$ : :help","$ : use global","$ : ls"]
    count=0
    for i in range(len(key_list)):
     send_keys_and_enter(action_chains, key_list[i])
     time.sleep(1)
     truncate_boxes = driver.find_elements(By.CSS_SELECTOR, ".history-item")  # 使用合适的选择器定位元素（注意使用复数形式的 find_elements）
    for truncate_box in truncate_boxes:
        text_content = truncate_box.text
       
        time.sleep(2)
        if test_list[count]!=text_content :
           print(test_list[count],text_content)
           T=False
        count+=1
           
           




    
    
    
    
    
    assert T
