from selenium.webdriver.common.by import By
from pages.common import CommonOps


class Home(CommonOps):

    # Locators
    FORM_AUTH = (By.LINK_TEXT, "Form Authentication")
    DYNAMIC_CONTROL = (By.LINK_TEXT, "Dynamic Controls")
    ADD_REMOVE = (By.LINK_TEXT, "Add/Remove Elements")

    # Actions
    def navigate_to_form_page(self):
        self.wait_for(self.FORM_AUTH).click()

    def navigate_to_dynamic_controls_page(self):
        self.wait_for(self.DYNAMIC_CONTROL).click()

    def navigate_to_add_remove_page(self):
        self.wait_for(self.ADD_REMOVE).click()
