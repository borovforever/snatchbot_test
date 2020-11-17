from base.base_class import BaseClass
from base.locators import MainPageLocators
from base.locators import BotLocators
import allure
import settings
import time


class CreateBot(BaseClass):
    bot_name = "test_bot"
    bot_descr = "Test_Bot_Description"

    def create_bot(self):
        self.find_element(BotLocators.MY_BOTS_SECTION).click()
        self.find_element(BotLocators.CREATE_BOT_BTN).click()
        blank_bot = self.find_element(BotLocators.BLANK_BOT_BTN)
        self.find_element2(blank_bot).perform()
        self.find_element3(BotLocators.BOT_NAME).send_keys(self.bot_name.title())
        self.find_element3(BotLocators.BOT_DESCRIPTION).send_keys(self.bot_descr)
        self.find_element3(BotLocators.UPLOAD_IMAGE).send_keys(settings.TEST_PIC)
        self.find_element(BotLocators.CREATE_BOT).click()
        ok_btn = self.find_element(BotLocators.OK_BTN)
        self.find_element2(ok_btn).perform()
        assert self.is_element_present(*BotLocators.ADD_INTERACTION_BTN), "No add new interaction button"
        test_bot = self.find_element(BotLocators.EMPTY_BOT)
        if test_bot:
            assert True
        else:
            self.allure_report()
            assert False, \
                f"{test_bot} failed! 'Bot isn't created"
