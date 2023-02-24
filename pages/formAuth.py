from selenium.webdriver.common.by import By

from .common import CommonOps



class FormAuthentication(CommonOps):

    FORM_AUTH_LOCATOR = (By.LINK_TEXT, "Form Authentication")
    FORM_USERNAME = (By.ID, "username")
    FORM_PASSWORD = (By.ID, "password")
    FORM_SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    FORM_ALERT = (By.ID, "flash")
    LOGOUT_BTN = (By.CLASS_NAME, "button")

    def navigate_to_form_page(self):
        self.wait_for(self.FORM_AUTH_LOCATOR).click()

    def enter_login_username(self, username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_login_password(self, password):
        self.find(self.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.FORM_SUBMIT_BTN).click()
    
    def check_login_logout_status(self):
        return self.wait_for(self.FORM_ALERT)
    
    def click_logout_button(self):
        self.find(self.LOGOUT_BTN).click()