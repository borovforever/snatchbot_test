import settings
import pytest
import allure
from landings.main_page_bot import MainPageBot


@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_bot(browser):
    link = settings.MAIN_PAGE
    page = MainPageBot(browser, link)
    page.open()
    page.main_page_bot()
