from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Webdisplayer:
    browser = None
    room_id = None
    chromedriver = Service(config('DRIVERPATH', default='/usr/lib/chromium-browser/chromedriver'))

    @classmethod
    def start(cls, url):
        if cls.browser is None:
            extset = ['enable-automation', 'ignore-certificate-errors']

            chrome_options = Options()
            # chrome_options.add_argument('--headless')  # 無視窗
            # chrome_options.add_argument('use-fake-ui-for-media-stream')
            chrome_options.add_argument("--kiosk") #全螢幕+app模式
            # chrome_options.add_argument("--start-fullscreen") # 全螢幕
            chrome_options.add_argument('--incognito')  # 無痕
            chrome_options.add_argument('--no-sandbox')  # 解決DevToolsActivePort檔案不存在的報錯
            chrome_options.add_experimental_option("excludeSwitches", extset)
            cls.browser = webdriver.Chrome(service=cls.chromedriver, options=chrome_options)
            cls.browser.get(f'{url}')

    @classmethod
    def stop(cls):
        if cls.browser is not None:
            # hangup_button = cls.browser.find_element(By.ID, 'hangup')
            # hangup_button.click()
            cls.browser.quit()
            cls.browser, cls.room_id = None, None


if __name__ == '__main__':
    Webdisplayer.start('https://www.cwb.gov.tw/V8/C/')
    input()
    Webdisplayer.stop()
