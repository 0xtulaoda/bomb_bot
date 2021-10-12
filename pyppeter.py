import asyncio
from pyppeteer import launch
import config
import time


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    element = await page.querySelector('h1')
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
class Browser():
    def __init__(self):
        EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'
        options = webdriver.ChromeOptions()
        options.add_extension(config.extencion)
        options.add_argument(
            f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')
        driver = webdriver.Chrome(executable_path=config.driver,options=options)
        driver.maximize_window()
        action = webdriver.ActionChains(driver)
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
        #driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/notification.html#connect/')
        time.sleep(2)
        # driver.find_element_by_xpath('//button[text()="Далее"]').click()
        # time.sleep(2)
        # driver.find_element_by_xpath('//button[text()="Подключиться"]').click()
        # time.sleep(10)


        driver.get('https://app.bombcrypto.io')
        #driver.get('http://www.google.com')
        driver.add_cookie(
            {'name': '_ga', 'value': 'GA1.1.1363365317.1633991225', 'domain':'.bombcrypto.io','expires': '2023-10-11T23:07:18.000Z' })
        driver.add_cookie(
            {'name': '_ga_K7PC8BCRLH', 'value': 'GS1.1.1633993468.2.1.1633993638.60','domain':'.bombcrypto.io','expires': '2023-10-11T23:07:18.000Z',
             })
        driver.get('https://app.bombcrypto.io')
        time.sleep(25)
        action.move_by_offset(529, 456).click().perform()
        time.sleep(3)
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/notification.html#connect/')
        time.sleep(3)
        driver.find_element_by_xpath('//button[text()="Далее"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//button[text()="Подключиться"]').click()
        time.sleep(10)
        time.sleep(5000)
        q=1
if __name__ == '__main__':
    browser = Browser()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
