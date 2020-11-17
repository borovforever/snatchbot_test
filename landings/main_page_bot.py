from selenium.webdriver.common.by import By

from base.base_class import BaseClass
from base.locators import MainPageLocators
import time


class MainPageBot(BaseClass):

    bot_message1 = "igor"

    def main_page_bot(self):
        assert self.is_element_present(*MainPageLocators.WIDGET_OPEN_XPATH)
        bot = self.find_element(MainPageLocators.WIDGET_OPEN_XPATH)
        self.find_element2(bot).perform()
        self.browser.switch_to.frame(MainPageLocators.CHAT_IFRAME)
        assert self.is_element_present(*MainPageLocators.BOT_MESSAGE), "No message from bot"
        self.find_element(MainPageLocators.TESTCHAT_INPUT_XPATH).send_keys(self.bot_message1.title())
        self.find_element(MainPageLocators.TESTCHAT_SEND_XPATH).click()
        test_widget = self.find_element(MainPageLocators.USER_MESSAGE)
        assert test_widget.text == "Yes", \
                f"Test failed! 'Embed chat' didn't answer'"



