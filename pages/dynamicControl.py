from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .common import CommonOps


class DynamcControls(CommonOps):
    # Locators
    CHECKBOX_LOCATOR = (By.XPATH, "//input[@type='checkbox']")
    INPUT_TEXT_LOCATOR = (By.XPATH, "//input[@type='text']")
    STATE_CHANGE_LOCATOR = (By.ID, "message")

    # Actions
    def check_checkbox_element(self):
        try:
            self.wait_for(self.CHECKBOX_LOCATOR)
            return ("Checkbox Element Presents")
        except TimeoutException:
            return ("No Checkbox Element")

    def checking_input_text_element(self):
        return self.wait_for(self.INPUT_TEXT_LOCATOR).is_enabled()

    def click_control_button(self, element):
        if element == "checkbox" or element == "input":
            control_xpath = f"//form[@id='{element}-example']/button"
        else:
            return "Element not Found"

        self.find((By.XPATH, control_xpath)).click()
        self.wait_for(self.STATE_CHANGE_LOCATOR)
