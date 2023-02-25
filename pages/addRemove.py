from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .common import CommonOps


class AddRemoveElement(CommonOps):
    # Locators
    ADD_ELEMENT_BTN = (By.TAG_NAME, "button")
    DELETE_BTN = (By.CLASS_NAME, "added-manually")

    # Actions
    def click_add_element_button(self):
        self.wait_for(self.ADD_ELEMENT_BTN).click()

    def check_delete_button(self):
        try:
            return self.wait_for(self.DELETE_BTN)
        except TimeoutException:
            return "No Delete Button"

    def click_delete_button(self):
        self.find(self.DELETE_BTN).click()
