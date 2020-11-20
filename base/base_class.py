from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from base.locators import MainPageLocators
import allure
from allure_commons.types import AttachmentType
import time
import settings


class BaseClass():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def login_autotest(self):
        self.find_element3(MainPageLocators.EMAIL_INPUT).send_keys(settings.USER_LOGIN)
        self.find_element3(MainPageLocators.PASS_XPATH).send_keys(settings.USER_PASSWORD)
        self.find_element(MainPageLocators.SIGN_IN_XPATH).click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            self.allure_report()
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            self.allure_report()
            return True

        return False

    def find_element(self, locator, time_wait=10):
        try:
            time.sleep(1)
            return WebDriverWait(self.browser, time_wait).until(ec.element_to_be_clickable(locator),
                                                                message=f"Can't find element by locator {locator}")
        except:
            self.allure_report()
            return False

    def find_element2(self, locator2):
        try:
            return ActionChains(self.browser).move_to_element(locator2).click(locator2)
        except:
            self.allure_report()
            return False

    def find_element3(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(ec.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_element4(self, locator):
        try:
            return self.browser.find_element(locator)
        except:
            self.allure_report()
            return False

    def find_element5(self, locator):
        try:
            return self.browser.find_elements_by_xpath(locator)
        except:
            self.allure_report()
            return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            self.allure_report()
            return False

        return True

    def allure_report(self):
        allure.attach(self.browser.get_screenshot_as_png(), name="testEmbedScreen",
                      attachment_type=AttachmentType.PNG)
