import settings
import pytest
import allure
from bot.create_bot import CreateBot


@allure.severity(allure.severity_level.CRITICAL)
def test_create_bot(browser):
    link = settings.LOGIN_PAGE
    bot = CreateBot(browser, link)
    bot.open()
    bot.login_create_bot()
    bot.create_bot()
    bot.copy_bot()
    bot.delete_bot()

