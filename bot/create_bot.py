from selenium.webdriver.common.keys import Keys

from base.base_class import BaseClass
from base.locators import MainPageLocators
from base.locators import BotLocators
import allure
import settings
import time


class CreateBot(BaseClass):

    bot_name = "test_bot"
    bot_descr = "Test_Bot_Description"
    delete_message = "delete"

    def try_delete(self):
        self.find_element(BotLocators.DELETE_BTN).click()
        self.find_element3(BotLocators.DELETE_INPUT).send_keys(self.delete_message)
        self.is_element_present(*BotLocators.DELETE_CONFIRM_BTN)
        self.find_element(BotLocators.DELETE_CONFIRM_BTN).click()
        # self.find_element(BotLocators.DELETE_CONFIRM_BTN).send_keys(Keys.TAB)
        # self.find_element(BotLocators.DELETE_CONFIRM_BTN).send_keys(Keys.TAB)
        # self.find_element(BotLocators.DELETE_CONFIRM_BTN).send_keys(Keys.ENTER)

    def go_to_my_bots(self):
        self.find_element(BotLocators.DASHBOARD).click()
        self.find_element(BotLocators.MY_BOTS_SECTION).click()

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
        self.find_element(BotLocators.MY_BOTS_SECTION).click()
        assert self.is_element_present(*BotLocators.BOT_CARD), "No bot found. Bot is not created"

    def copy_bot(self):
        bot_card = self.find_all_elements(BotLocators.BOT_MENU)
        bot_card[0].click()
        self.find_element(BotLocators.COPY_BOT_BTN).click()
        self.go_to_my_bots()
        assert self.is_element_present(*BotLocators.BOT_CARD), "No bot is copied"

    def delete_bot(self):
        bot_card = self.find_all_elements(BotLocators.BOT_MENU)
        bot_card[0].click()
        self.try_delete()
        self.go_to_my_bots()
        self.find_element(BotLocators.BOT_MENU).click()
        self.try_delete()
        self.go_to_my_bots()
        assert self.is_not_element_present(*BotLocators.BOT_CARD), "Bot isn't deleted"
        no_bots = self.find_element(BotLocators.NO_BOTS_MESSAGE)
        assert no_bots.text == "Your bots will be displayed here", "No text 'Your bots will be displayed here' is " \
                                                                   "found."
