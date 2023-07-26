import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import BaseCase
@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()


class TestHistory(BaseCase):
    def send_keys_and_enter(self, action_chains, keys):
        action_chains.send_keys(keys)
        try:
            action_chains.key_down(Keys.COMMAND)
        except:
            action_chains.key_down(Keys.CONTROL)
        action_chains.key_down(Keys.ENTER)
        action_chains.perform()

    def test_history_display(self): 
        
        T = True
        self.driver.get('http://34.28.121.9:14240/gsql/')
        time.sleep(5)

        # 找到 CodeMirror 元素
        codeMirror = self.driver.find_element(By.CSS_SELECTOR, ".CodeMirror")

        # 创建动作链对象
        action_chains = ActionChains(self.driver)

        action_chains.click(codeMirror).perform()

        # 判断history是否有新一条显示
        key_list = ["use test1", "ls",'ls','ls']
        test_list=["$ : :help","$ : use test1","$ : ls",'$ : ls','$ : ls']
        count=0
        for i in range(len(key_list)):
            self.send_keys_and_enter(action_chains, key_list[i])
            time.sleep(1)
        truncate_boxes = self.driver.find_elements(By.CSS_SELECTOR, ".history-item")  # 使用合适的选择器定位元素（注意使用复数形式的 find_elements）
        for truncate_box in truncate_boxes:
            text_content = truncate_box.text
            #print(text_content)
            time.sleep(2)
            if test_list[count]!=text_content :
               T=False
            count+=1

        
        # 判断history的导航功能
        guiding_boxes = self.driver.find_elements(By.CSS_SELECTOR, ".history-item")
        action_chains.click(guiding_boxes[0]).perform()
        time.sleep(2)
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".command-preview")
        for element in elements:
            print(element.text)
            print(element.get_attribute("outerHTML"))
            
            # if element.is_displayed():
            #     print('yes')
            # else:
            #     print('no')
            
        
        assert T


