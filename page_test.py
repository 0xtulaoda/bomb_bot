from selenium import webdriver
import config
import time

driver = webdriver.Chrome(executable_path=config.driver,)
driver.get(r'C:\Users\Arsdm\OneDrive\Рабочий стол\Google.html')
driver.maximize_window()

time.sleep(1)
action = webdriver.ActionChains(driver)
action.move_by_offset(561, 273).click().perform()
action.click()
time.sleep(200)