import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = "D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    #driver.quit()

def test_login(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    # 找到用户名和密码输入框的元素
    username_input = driver.find_element(By.XPATH,'//*[@id="particles-js"]/div/div[2]/div/div/div/input')
    password_input = driver.find_element(By.XPATH,'//*[@id="particles-js"]/div/div[3]/div/div/div/input')

    # 输入用户名和密码
    username_input.send_keys("tigergraph")
    password_input.send_keys("tigergraph")

    # 模拟按下回车键提交表单
    password_input.send_keys(Keys.RETURN)

    try:
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/tools-head//div/div[1]/img')
    except:
        pytest.fail('Failed to log in')

    driver.quit()  # 关闭 WebDriver


 
    
    
