from base.base_class import BaseClass
from base.locators import MainPageLocators
import time


class MainPageBot(BaseClass):

    bot_message1 = "igor"

    def main_page_bot(self):
        lexi_bot = self.find_element(MainPageLocators.WIDGET_OPEN_XPATH)
        if lexi_bot:
            assert True
        else:
            self.allure_report()
            assert False, \
                f"Test failed! 'Embed chat' not found'"
        bot = self.find_element(MainPageLocators.WIDGET_OPEN_XPATH)
        self.find_element2(bot).perform()
        self.browser.switch_to.frame(MainPageLocators.CHAT_IFRAME)
        self.find_element(MainPageLocators.TESTCHAT_INPUT_XPATH).send_keys(self.bot_message1.title())
        self.find_element(MainPageLocators.TESTCHAT_SEND_XPATH).click()
        test_widget = self.find_element(MainPageLocators.USER_MESSAGE)
        assert test_widget.text == "Yes", \
                f"Test failed! 'Embed chat' didn't answer'"



