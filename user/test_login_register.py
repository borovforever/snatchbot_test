import settings
import pytest
import allure
from user.register_login import UserRegister


@allure.severity(allure.severity_level.CRITICAL)
def test_register_login(browser):
    link = settings.REGISTER_PAGE
    page = UserRegister(browser, link)
    page.open()
    page.registration()
    page.already_registered()
    page.login_delete_account()