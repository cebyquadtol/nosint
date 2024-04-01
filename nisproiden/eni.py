from selenium.webdriver.common.by import By

cancel_btn = (By.XPATH, '//button[contains(text(), "Cancel")]')
click_Xpath(driver, 2, cancel_btn)
