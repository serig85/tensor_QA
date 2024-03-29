from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .logger import Logger
from .locators import BasePageLocation


log = Logger().loggen()


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def close_cookies_mess_sbis(self):
        try:
            WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(BasePageLocation.block_mes_cookies_sbis))
            cookies = (self.browser.find_element
                       (*BasePageLocation.close_mes_cookies_sbis))
            cookies.click()
        except StaleElementReferenceException:
            log.info("No sbis Cookies")

    def close_cookies_mess_tensor(self):
        try:
            WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(BasePageLocation.block_mes_cookies_tensor))
            cookies = WebDriverWait(self.browser, 10).until(
                ec.presence_of_element_located(BasePageLocation.close_mes_cookies_tensor))
            cookies.click()
        except StaleElementReferenceException:
            log.info("No tensor Cookies ")
