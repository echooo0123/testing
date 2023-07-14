from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    driver.get('http://34.28.121.9:14240/gsql/')

    # 找到用户名和密码输入框的元素
    wait = WebDriverWait(driver, 10)  # 设置等待时间为10秒
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="particles-js"]/div/div[2]/div/div/div/input')))
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="particles-js"]/div/div[3]/div/div/div/input')))

    # 输入用户名和密码
    username_input.send_keys("tigergraph")
    password_input.send_keys("tigergraph")

    # 模拟按下回车键提交表单
    password_input.send_keys(Keys.RETURN)

    # 验证登录成功后的页面是否正确显示
    dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div/div/div[1]/div[1]/div/div/div[2]/div/svg')))

# 创建浏览器驱动并运行测试
driver = webdriver.Chrome("D:\chromedriver.exe")
test_login(driver)
driver.quit()
