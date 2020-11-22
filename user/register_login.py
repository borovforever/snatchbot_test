from selenium.webdriver.common.by import By
import settings
from base.base_class import BaseClass
from base.locators import UserLocators
from base.locators import MainPageLocators
from selenium.webdriver.chrome.options import Options
import time


class UserRegister(BaseClass):
    first_name = "test"
    last_name = "test2"
    email = 'snatchtest@mailforspam.com'
    not_valid_pass = "monadsasd"

    def login_faled(self):
        self.find_element3(MainPageLocators.EMAIL_INPUT).send_keys(settings.USER_LOGIN)
        self.find_element3(MainPageLocators.PASS_XPATH).send_keys(self.not_valid_pass)
        self.find_element(MainPageLocators.SIGN_IN_XPATH).click()

    def registration(self):
        self.find_element3(UserLocators.FIRSTNAME).send_keys(self.first_name)
        self.find_element3(UserLocators.LAST_NAME).send_keys(self.last_name)
        self.find_element3(UserLocators.EMAIL).send_keys(self.email)
        self.find_element3(UserLocators.PASSWORD).send_keys(settings.USER_PASSWORD)
        self.find_element(UserLocators.SIGN_UP_BTN).click()
        user_registered = self.find_element(UserLocators.GREAT_MESSAGE)
        assert user_registered.text == self.email, "User isn't registered"
        self.browser.get(settings.EMAIL_REG)
        check = self.find_element(UserLocators.CHECK_BTN)
        self.find_element2(check).perform()
        email = self.find_all_elements(UserLocators.FIRST_EMAIL)
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
        assert self.is_element_present(*UserLocators.DASHBOARD_TITLE), "No 'Dashboard', login unsuccessful"
        self.find_element(UserLocators.PROFILE).click()
        self.find_element(UserLocators.DELETE_ACCOUNT).click()
        self.find_element(UserLocators.CONFIRM_DEL).click()
        assert self.is_element_present(*UserLocators.SIGN_IN_XPATH), "Account is not deleted"
        self.find_element3(UserLocators.EMAIL_LOGIN).send_keys(self.email)
        self.find_element3(UserLocators.PASS_LOGIN).send_keys(settings.USER_PASSWORD)
        self.find_element(UserLocators.SIGN_IN_XPATH).click()
        assert self.is_not_element_present(*UserLocators.DASHBOARD_TITLE), "Login completed, account isn't deleted."
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

    def login_with_socials(self):
        self.browser.get(settings.LOGIN_PAGE)
        assert self.is_element_present(*UserLocators.LOGIN_GOOGLE), "No 'login with Google' button"
        assert self.is_element_present(*UserLocators.LOGIN_FB), "No 'login with Facebook' button"
        self.find_element(UserLocators.LOGIN_GOOGLE).click()
        self.find_element3(UserLocators.NAME_GOOGLE).send_keys(settings.LOGIN_GOOGLE)
        self.find_element(UserLocators.NEXT_LOGIN_GOOGLE).click()
        self.find_element3(UserLocators.GOOGLE_PASS).send_keys(settings.PASSWORD_GOOGLE)
        self.find_element(UserLocators.NEXT_PASS_GOOGLE).click()
        assert self.is_element_present(*UserLocators.DASHBOARD_TITLE), "Login with Google unsuccessful. No Dasboard " \
                                                                       "is present "
        self.find_element(UserLocators.LOGOUT).click()
        assert self.is_element_present(*UserLocators.LOG_IN_TITLE), "Logout unsuccessful."
        self.find_element(UserLocators.LOGIN_FB).click()
        self.find_element3(UserLocators.FB_EMAIL).send_keys(settings.LOGIN_FB)
        self.find_element3(UserLocators.FB_PASS).send_keys(settings.PASSWORD_FB)
        self.find_element(UserLocators.LOGIN_IN_FB).click()
        self.find_element(UserLocators.AS_CONTINUE_FB).click()
        assert self.is_element_present(*UserLocators.DASHBOARD_TITLE), "Login with Facebook unsuccessful. No Dasboard " \
                                                                       "is present."
        self.find_element(UserLocators.LOGOUT).click()
        assert self.is_element_present(*UserLocators.LOG_IN_TITLE), "Logout unsuccessful."

    def login_with_not_valid_password(self):
        self.login_faled()
        assert self.is_not_element_present(*UserLocators.DASHBOARD_TITLE), "Login with invalid password"
        assert self.is_element_present(
            *UserLocators.INVALID_EMAIL_MODAL), "No modal window 'Invalid email or password' is displayed"
        message = self.find_element(*UserLocators.INVALID_EMAIL_MESSAGE)
        assert message.text == "Invalid email or password", "No 'invalid email or password message'."
