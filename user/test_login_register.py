import settings
import pytest
import allure
from user.register_login import UserRegister


@allure.severity(allure.severity_level.CRITICAL)
def test_register_login_delete(browser):
    link = settings.REGISTER_PAGE
    page = UserRegister(browser, link)
    page.open()
    page.registration()
    page.already_registered()
    page.login_delete_account()


def test_login_with_socials(browser):
    link = settings.LOGIN_PAGE
    page = UserRegister(browser, link)
    page.open()
    page.login_with_socials()


def test_login_with_not_valid_password(browser):
    link = settings.LOGIN_PAGE
    page = UserRegister(browser, link)
    page.open()
    page.login_with_not_valid_password()
