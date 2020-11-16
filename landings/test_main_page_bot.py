import settings
import pytest
from landings.main_page_bot import MainPageBot


def test_main_page_bot(browser):
    link = settings.MAIN_PAGE
    page = MainPageBot(browser, link)
    page.open()
    page.main_page_bot()