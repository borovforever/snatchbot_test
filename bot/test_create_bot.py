import settings
import pytest
from bot.create_bot import CreateBot

def test_create_bot(browser):
    link = settings.LOGIN_PAGE
    bot = CreateBot(browser, link)
    bot.open()
    bot.create_bot()
