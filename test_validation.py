from pages.dynamicControl import DynamcControls
from pages.formAuth import FormAuthentication
from pages.addRemove import AddRemoveElement



def test_form_authentication(driver):
    form = FormAuthentication(driver)

    form.navigate_to_form_page()
    form.enter_login_username("tomsmith")
    form.enter_login_password("SuperSecretPassword!")
    form.click_login_button()

    assert "logged in" in form.check_login_logout_status().text 

    form.click_logout_button()
    assert "logged out" in form.check_login_logout_status().text

def test_add_remove_element(driver):
    add_rem = AddRemoveElement(driver)
    add_rem.navigate_to_add_remove_page()
    add_rem.click_add_element_button()
    delete_button = add_rem.check_delete_button().text
    assert delete_button == "Delete"

    add_rem.click_delete_button()
    delete_button = add_rem.check_delete_button()
    assert delete_button == "No Delete Button"

    
def test_dynamic_control_checkbox(driver):
    checkbox = DynamcControls(driver)
    checkbox.navigate_to_dynamic_controls_page()

    assert checkbox.check_checkbox_element() == "Checkbox Element Presents"
    checkbox.click_control_button("checkbox")

    assert checkbox.check_checkbox_element() == "No Checkbox Element"

    checkbox.click_control_button("checkbox")
    
    assert checkbox.check_checkbox_element() == "Checkbox Element Presents"

def test_dynamic_control_input_text(driver):
    input_text = DynamcControls(driver)
    input_text.navigate_to_dynamic_controls_page()
    
    assert input_text.checking_input_text_element() == False

    input_text.click_control_button("input")
    
    assert input_text.checking_input_text_element() == True

    input_text.click_control_button("input")

    assert input_text.checking_input_text_element() == False