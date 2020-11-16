from base.base_class import BaseClass
from base.locators import MainPageLocators
from base.locators import BotLocators
import allure
import settings
import time

@allure.severity(allure.severity_level.CRITICAL)
class CreateBot(BaseClass):

    def create_bot(self):
        self.find_element3(MainPageLocators.EMAIL_INPUT).send_keys(settings.USER_LOGIN)
        self.find_element3(MainPageLocators.PASS_XPATH).send_keys(settings.USER_PASSWORD)
        self.find_element(MainPageLocators.SIGN_IN_XPATH).click()
        self.find_element(BotLocators.MY_BOTS_SECTION).click()
        self.find_element(BotLocators.CREATE_BOT_BTN).click()
        self.find_element(BotLocators.BLANK_BOT_BTN).click()
        button = self.find_element(BotLocators.BUTTON_ACTIVITY)
        button_disabled = button.get_attribute("disabled")
        print("value of button Submit: ", button_disabled)
        if button_disabled is not None:
            assert True
        else:
            self.allure_report()
            assert False, \
                f"Test{button_disabled} failed! 'Create' button is active."
        self.find_element3(B)
        time.sleep(5)

