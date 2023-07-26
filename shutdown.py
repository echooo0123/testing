def shutdown(driver):
    driver.get('http://34.28.121.9:14240/gsql/')
    time.sleep(5)
    container = driver.find_element(By.CSS_SELECTOR, 'tools-head')
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", container)
    close_button = shadow_root.find_element(By.ID, 'close-btn')
    close_button.click()
    


    