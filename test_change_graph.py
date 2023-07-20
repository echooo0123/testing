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


@pytest.fixture
def driver():
    # 创建一个 Chrome WebDriver 实例
    options = Options()
    # 根据需要进行进一步的配置
    driver_path = r"D:\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    yield driver
    driver.quit()



def test_search_graph(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    
    interactive = driver.find_element(By.CSS_SELECTOR, ".graph-selector")
    action_chains = ActionChains(driver)
    action_chains.click(interactive).perform()
    T=True
    wait = WebDriverWait(driver, 10)

    check_boxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li[role="option"]')))
    for check_box in check_boxes:
        text_content = check_box.text
        if text_content == "communication_mau":
            check_box.click()
            time.sleep(2)
            break
    time.sleep(2)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".command-preview")))
    text = element.text
    if element.is_displayed() and text == "use graph communication_mau":
        pass
    else:
        print(element.is_displayed())
        print(text)
        T = False

    assert T

        
       
        
    



