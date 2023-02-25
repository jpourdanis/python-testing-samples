from pages.dynamicControl import DynamcControls
from pages.formAuth import FormAuthentication
from pages.addRemove import AddRemoveElement
from pages.home import Home


def test_form_authentication(driver):
    home_page = Home(driver)
    home_page.navigate_to_form_page()

    form_authentication_page = FormAuthentication(driver)
    form_authentication_page.enter_login_username("tomsmith")
    form_authentication_page.enter_login_password("SuperSecretPassword!")
    form_authentication_page.click_login_button()

    assert "logged in" in form_authentication_page.check_login_logout_status().text

    form_authentication_page.click_logout_button()

    assert "logged out" in form_authentication_page.check_login_logout_status().text


def test_add_remove_element(driver):
    home_page = Home(driver)
    home_page.navigate_to_add_remove_page()

    add_remove_element_page = AddRemoveElement(driver)
    add_remove_element_page.click_add_element_button()
    delete_button = add_remove_element_page.check_delete_button().text
    assert delete_button == "Delete"

    add_remove_element_page.click_delete_button()
    delete_button = add_remove_element_page.check_delete_button()
    assert delete_button == "No Delete Button"


def test_dynamic_control_checkbox(driver):
    home_page = Home(driver)
    home_page.navigate_to_dynamic_controls_page()

    dynamc_controls_page = DynamcControls(driver)

    assert dynamc_controls_page.check_checkbox_element() == "Checkbox Element Presents"
    dynamc_controls_page.click_control_button("checkbox")

    assert dynamc_controls_page.check_checkbox_element() == "No Checkbox Element"

    dynamc_controls_page.click_control_button("checkbox")

    assert dynamc_controls_page.check_checkbox_element() == "Checkbox Element Presents"


def test_dynamic_control_input_text(driver):
    home_page = Home(driver)
    home_page.navigate_to_dynamic_controls_page()

    dynamc_controls_page = DynamcControls(driver)

    assert dynamc_controls_page.checking_input_text_element() == False

    dynamc_controls_page.click_control_button("input")

    assert dynamc_controls_page.checking_input_text_element() == True

    dynamc_controls_page.click_control_button("input")

    assert dynamc_controls_page.checking_input_text_element() == False
