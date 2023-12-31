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

def click_tool_and_verify_url(driver,tool_index, expected_url):
    shutdown(driver)
    #driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    action_chains = ActionChains(driver)
    container = driver.find_element(By.CSS_SELECTOR, 'tools-head')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", container)
    svg_element = shadow_root.find_element(By.CSS_SELECTOR, 'svg.tools_apps-btn')
    svg_element.click()
    time.sleep(5)
    tool_button = shadow_root.find_elements(By.CSS_SELECTOR, '.tools_apps-item')[tool_index]
    action_chains.click(tool_button).perform()
    time.sleep(5)
    
    current_url = driver.current_url
    
    assert current_url == expected_url


    
def test_first_tool(driver):
    click_tool_and_verify_url(driver, 0, 'http://34.28.121.9:14240/studio/#/home')

def test_second_tool(driver):
    click_tool_and_verify_url(driver, 1, 'http://34.28.121.9:14240/insights/apps')
def test_third_tool(driver):
    click_tool_and_verify_url(driver, 2, "http://34.28.121.9:14240/gsql/")
def test_forth_tool(driver):
    click_tool_and_verify_url(driver, 3,  'http://34.28.121.9:14240/admin/#/dashboard')
def test_fifthtool(driver):
    click_tool_and_verify_url(driver, 4, 'http://34.28.121.9:14240/graphql/')
def test_sixthtool(driver):
    shutdown(driver)
    #driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    action_chains = ActionChains(driver)
    container = driver.find_element(By.CSS_SELECTOR, 'tools-head')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", container)
    svg_element = shadow_root.find_element(By.CSS_SELECTOR, 'svg.tools_apps-btn')
    svg_element.click()
    time.sleep(5)
    tool_button = shadow_root.find_element(By.CSS_SELECTOR,'.tools_apps-bottom')
    action_chains.click(tool_button).perform()
    time.sleep(5)
    expected_url='http://34.28.121.9:14240/#/apps'
    current_url = driver.current_url
    assert current_url == expected_url

    