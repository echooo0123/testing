import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from shutdown import shutdown


@pytest.fixture
def driver():
     # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()
def click_tool_and_verify_url(driver,tool_index,mode, expected_url):
    shutdown(driver)
    #driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    action_chains = ActionChains(driver)
    container = driver.find_element(By.CSS_SELECTOR, 'tools-head')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", container)
    svg_element = shadow_root.find_element(By.CSS_SELECTOR, 'img.tools-head-icon')
    svg_element.click()
    time.sleep(5)
    tool_button = shadow_root.find_elements(By.CSS_SELECTOR, '.desc')[tool_index]
    action_chains.click(tool_button).perform()
    time.sleep(5)
    if mode==1:
        driver.switch_to.window(driver.window_handles[-1])
    current_url = driver.current_url
    
    
    assert current_url == expected_url
def test_zero_tool(driver):
    shutdown(driver)
    #driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    container = driver.find_element(By.CSS_SELECTOR, 'tools-head')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", container)
    svg_element = shadow_root.find_element(By.CSS_SELECTOR, 'img.tools-head-icon')
    svg_element.click()
    time.sleep(5)
    tool_button = shadow_root.find_elements(By.CSS_SELECTOR, '.desc')[0]
    print(tool_button.text)
    assert tool_button.text=="tigergraph"
    
def test_first_tool(driver):
    click_tool_and_verify_url(driver, 1,0,'http://34.28.121.9:14240/#/login?returnURL=%2Fgsql%2F&loggedOut=true')
def test_second_tool(driver):
    click_tool_and_verify_url(driver, 2,1,'https://docs.tigergraph.com/tigergraph-server/current/gsql-shell/web')
def test_third_tool(driver):
     click_tool_and_verify_url(driver, 3,1,'https://docs.tigergraph.com/gui/current/graphstudio/patent-and-third-party-notice')
