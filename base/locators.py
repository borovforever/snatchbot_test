from selenium.webdriver.common.by import By


class MainPageLocators():
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASS_XPATH = (By.XPATH, "//input[@name='password']")
    SIGN_IN_XPATH = (By.XPATH, "//button[@data-test='sign_in_btn']")
    WIDGET_OPEN_XPATH = (By.XPATH, "//div[@id='sntch_button']")
    WIDGET_CLOSE_XPATH = (By.XPATH, "//div[@id='sntch_close']")
    CHAT_IFRAME = "sntch_iframe"
    POPUP_IFRAME = "sntch_popup"
    TESTCHAT_INPUT_XPATH = (By.XPATH, "//input[@data-test='input-chat']")
    TESTCHAT_SEND_XPATH = (By.XPATH, "//button[@data-test='btn-send-message']")
    BOT_MESSAGE = (By.XPATH, "//div[@data-test='message-text']")
    USER_MESSAGE = (By.XPATH, "//span[contains(text(),'Yes')]")

class BotLocators():
    MY_BOTS_SECTION = (By.XPATH, "//a[@data-test='route-bots']")
    BOT_MENU = (By.XPATH, ".//*[@data-test='bot-action-menu']")
    CREATE_BOT_BTN = (By.XPATH, "//button[@data-test='btn-create-bot']")
    BLANK_BOT_BTN = (By.XPATH, "//*[@data-test='templates-item']")
    BUTTON_ACTIVITY = (By.XPATH, "//button[@disabled='true']")
    BOT_NAME = (By.XPATH, "//textarea[@data-test='bot-name']")
    BOT_DESCRIPTION = (By.XPATH, "//textarea[@data-test='bot-description']")
    UPLOAD_IMAGE = (By.XPATH, "//input[@data-test='input-file']")
    CREATE_BOT = (By.XPATH, "//button[@data-test='btn-create-bot']")
    OK_BTN = (By.XPATH, "//button[@data-test='btn-alert-modal2']")
    ADD_INTERACTION_BTN = (By.XPATH, "//button[@data-test='btn-add-interaction']")
    EMPTY_BOT = (By.XPATH, "//div[@class='conversation__empty-plugin--is-empty']")
    CANCEL_BOT_BTN = (By.XPATH, "////span[@translate='buttons.cancel']")
    TEMPLATE_CARD = (By.XPATH, "//div[@class='view directory-view']")
    USE_TEMPLATE = (By.XPATH, "//button[@class='mat-stroked-button mat-button-base']")
    TEST_CHAT_IFRAME = "sntch_iframe"
    PERSISTENT_MENU_BTN = (By.XPATH, "//button[@class='persistent-menu-btn mat-menu-trigger mat-icon-button mat-button-base']")
    PERSISTENT_XPATH = (By.XPATH, "//button[@role='menuitem']")
    EDIT_BOT = (By.XPATH, "//button[@data-test='bot-action-edit']")
    add_new_interaction_xpath = "//span[contains(text(),'Add new interaction / plugin')]"
    interaction_name_xpath = "//input[@data-test='input-iteraction-name']"
    create_interaction_btn_xpath = "//button[@data-test='btn-create-iteraction']"
    bot_message_xpath = "//textarea[@data-test='initial-response-message']"
    open_testchat_xpath = "//div[@id='sntch_button']"
    test_chat_slider_xpath = "//mat-slide-toggle[@data-test='toggle-test-chat']"
    test_chat_refresh_xpath = "//mat-icon[contains(text(),'autorenew')]"
    test_chat_highlight_extracted = "//mat-icon[contains(text(),'subtitles')]"
    test_chat_toggle_xpath = "//mat-slide-toggle[@data-test='toggle-test-chat']"
    delete_btn_xpath = "//button[@data-test='bot-action-delete']"
    delete_input_xpath = "//input[@data-test='bot-delete-input']"
    delete_confirm_xpath = "//button[@data-test='bot-delete-confirm']"
    cancel_btn_xpath = "//button[@data-test='bot-delete-cancel']"
    copy_bot_btn_xpath = "//button[@data-test='bot-action-copy']"
    bot_configure_xpath = "//button[@data-test='bot-action-configure']"
    configure_name_xpath = "//input[@formcontrolname='name']"
    configure_description_xpath = "//input[@formcontrolname='description']"
    bot_lang_dropdown = "//div[@class='language-bot']"
    dutch_lang_xpath = "//mat-option[@ng-reflect-value='82']"
    change_pic_xpath = "//input[@type='file']"
    widget_open_xpath = "//div[@id='sntch_button']"
    widget_close_xpath = "//div[@id='sntch_close']"
