from selenium.webdriver.common.by import By
import settings
from base.base_class import BaseClass
from base.locators import UserLocators
import time


class UserRegister(BaseClass):

    first_name = "test"
    last_name = "test2"
    email = 'snatchtest@mailforspam.com'

    def registration(self):
        self.find_element3(UserLocators.FIRSTNAME).send_keys(self.first_name)
        self.find_element3(UserLocators.LAST_NAME).send_keys(self.last_name)
        self.find_element3(UserLocators.EMAIL).send_keys(self.email)
        self.find_element3(UserLocators.PASSWORD).send_keys(settings.USER_PASSWORD)
        self.find_element(UserLocators.SIGN_UP_BTN).click()
        assert self.is_element_present(*UserLocators.GREAT_MESSAGE), "No 'Great, Check your Inbox Message'"
        self.browser.get(settings.EMAIL_REG)
        check = self.find_element(UserLocators.CHECK_BTN)
        self.find_element2(check).perform()
        email = self.find_element5(UserLocators.FIRST_EMAIL)
        email[0].click()
        assert self.is_element_present(*UserLocators.EMAIL_VERIFY), "No 'Confirm' button"
        self.find_element(UserLocators.EMAIL_VERIFY).click()
        assert self.is_element_present(*UserLocators.ACCOUNT_VERIFIED_MESSAGE), "No 'Thank you, your account has " \
                                                                                "been verified' message' "
        self.find_element(UserLocators.OK_BTN).click()
        assert self.is_element_present(*UserLocators.LOG_IN_TITLE), "No login page is opened"

    def login_delete_account(self):
        self.browser.get(settings.LOGIN_PAGE)
        self.find_element3(UserLocators.EMAIL_LOGIN).send_keys(self.email)
        self.find_element3(UserLocators.PASS_LOGIN).send_keys(settings.USER_PASSWORD)
        self.find_element(UserLocators.SIGN_IN_XPATH).click()
        assert self.is_element_present(*UserLocators.DASHBOARD_TITLE), "No 'Dashboard'"
        self.find_element(UserLocators.PROFILE).click()
        self.find_element(UserLocators.DELETE_ACCOUNT).click()
        self.find_element(UserLocators.CONFIRM_DEL).click()
        assert self.is_element_present(*UserLocators.SIGN_IN_XPATH), "Account is not deleted"
        self.find_element3(UserLocators.EMAIL_LOGIN).send_keys(self.email)
        self.find_element3(UserLocators.PASS_LOGIN).send_keys(settings.USER_PASSWORD)
        self.find_element(UserLocators.SIGN_IN_XPATH).click()
        assert self.is_element_present(
            *UserLocators.ACCOUNT_VERIFIED_MESSAGE), "No 'Invalid email or password' message."

    def already_registered(self):
        self.browser.get(settings.REGISTER_PAGE)
        self.find_element3(UserLocators.FIRSTNAME).send_keys(self.first_name)
        self.find_element3(UserLocators.LAST_NAME).send_keys(self.last_name)
        self.find_element3(UserLocators.EMAIL).send_keys(self.email)
        self.find_element3(UserLocators.PASSWORD).send_keys(settings.USER_PASSWORD)
        self.find_element(UserLocators.SIGN_UP_BTN).click()
        assert self.is_element_present(
            *UserLocators.USER_REGISTERED_MESSAGE), "No 'User with this email is already registered' message."
