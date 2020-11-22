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
    DASHBOARD = (By.XPATH, "//a[@data-test='route-dashboard']")
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
    CANCEL_BOT_BTN = (By.XPATH, ".//*[@data-test='bot-delete-cancel']")
    BOT_CARD = (By.XPATH, "//div[@data-test='bot-title']")
    COPY_BOT_BTN = (By.XPATH, "//button[@data-test='bot-action-copy']")
    DELETE_BTN= (By.XPATH, "//button[@data-test='bot-action-delete']")
    DELETE_INPUT = (By.XPATH, "//input[@data-test='bot-delete-input']")
    DELETE_CONFIRM_BTN = (By.XPATH, "//button[@data-test='bot-delete-confirm']")
    NO_BOTS_MESSAGE = (By.XPATH, "//h2[@class='no-bots__title']")


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

    bot_configure_xpath = "//button[@data-test='bot-action-configure']"
    configure_name_xpath = "//input[@formcontrolname='name']"
    configure_description_xpath = "//input[@formcontrolname='description']"
    bot_lang_dropdown = "//div[@class='language-bot']"
    dutch_lang_xpath = "//mat-option[@ng-reflect-value='82']"
    change_pic_xpath = "//input[@type='file']"
    widget_open_xpath = "//div[@id='sntch_button']"
    widget_close_xpath = "//div[@id='sntch_close']"


class UserLocators():
    FIRSTNAME = (By.XPATH, "//*[@data-test='firstname']")
    LAST_NAME = (By.XPATH, "//*[@data-test='lastname']")
    EMAIL = (By.XPATH, "//input[@data-test='email']")
    PASSWORD = (By.XPATH, "//input[@data-test='password']")
    SIGN_UP_BTN = (By.XPATH, "//button[@data-test='btn-submit']")
    GREAT_MESSAGE = (By.XPATH, "//div[@class='check_email_msg']")
    MAIL_FOR_SPAM = (By.XPATH, "//input[@name='spammail']")
    CHECK_BTN = (By.XPATH, "//input[@id='button']")
    EMAIL_VERIFY = (By.XPATH, "//a[contains(text(),'https://cpstaging.snatch.cloud/auth/check_email?to')]")
    ACCOUNT_VERIFIED_MESSAGE = (By.XPATH, "//p")
    OK_BTN = (By.XPATH, "//button[@data-test='btn-alert-modal2']")
    LOG_IN_TITLE = (By.XPATH, "//h2")
    INVALID_EMAIL_MODAL = (By.XPATH, "//div[@data-test='alert-modal2']")
    INVALID_EMAIL_MESSAGE = (By.XPATH, "//p[@style='word-break: break-word']")
    DASHBOARD_TITLE = (By.XPATH, "//div[@class='dashboard__title']")
    SIGN_IN_XPATH = (By.XPATH, "//button[@data-test='sign_in_btn']")
    EMAIL_LOGIN = (By.XPATH, "//input[@data-test='login_email_input']")
    PASS_LOGIN = (By.XPATH, "//input[@data-test='login_password_input']")
    PROFILE = (By.XPATH, "//a[@data-test='profile_router_link']")
    DELETE_ACCOUNT = (By.XPATH, "//button[@data-test='delete_account_btn']")
    USER_REGISTERED_MESSAGE = (By.XPATH, "//p[@style]")
    CONFIRM_DEL = (By.XPATH, "//button[@data-test='confirm-alert']")
    FIRST_EMAIL = (By.XPATH, "//a[contains(text(),'Confirm your email address ')]")
    LOGIN_FB = (By.XPATH, "//button[@class='btn-facebook mat-stroked-button mat-button-base']")
    LOGIN_GOOGLE = (By.XPATH, "//button//span[contains(text(),'Login with Google')]")
    NAME_GOOGLE = (By.XPATH, "//input[@name='identifier']")
    NEXT_LOGIN_GOOGLE = (By.XPATH, "//div[@id='identifierNext']")
    GOOGLE_PASS = (By.XPATH, "//input[@name='password']")
    NEXT_PASS_GOOGLE = (By.XPATH, "//div[@id='passwordNext']")
    LOGOUT = (By.XPATH, "//mat-icon[@ng-reflect-message='Logout']")
    FB_EMAIL = (By.XPATH, "//input[@name='email']")
    FB_PASS = (By.XPATH, "//input[@name='pass']")
    LOGIN_IN_FB = (By.XPATH, "//button[@name='login']")
    AS_CONTINUE_FB = (By.XPATH, "//span[contains(text(),'Продолжить как Jake Stark')]")




