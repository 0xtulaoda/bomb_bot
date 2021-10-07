from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import time

class Browser():
    def __init__(self):
        EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'
        options = webdriver.ChromeOptions()
        options.add_extension(config.extencion)

        driver = webdriver.Chrome(executable_path=config.driver,options=options)
        driver.maximize_window()

       # driver.get('http://www.google.com')
        time.sleep(6)
        driver.switch_to.window(driver.window_handles[0])
        q=1
        driver.find_element_by_xpath('//button[text()="Начать работу"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//button[text()="Импортировать кошелек"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//button[text()="Нет, спасибо"]').click()
        time.sleep(1)


        inputs = driver.find_elements_by_xpath('//input')
        inputs[0].send_keys('worry level interest gap tackle disease industry vacuum wear guide elevator voice')
        inputs[1].send_keys('KSAMATEM808')
        inputs[2].send_keys('KSAMATEM808')
        driver.find_element_by_css_selector('.first-time-flow__terms').click()
        time.sleep(2)
        driver.find_element_by_xpath('//button[text()="Импорт"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//button[text()="Выполнено"]').click()
        time.sleep(2)

        driver.get('http://www.google.com')
        time.sleep(2000)
if __name__ == '__main__':
    browser = Browser()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
