import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


@pytest.fixture
def _driver(request):
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=options)

    yield driver
    driver.close()


def test_submit_form_and_get_error_on_surname(_driver):
    url = "https://testpages.herokuapp.com/styled/validation/input-validation.html"
    _driver.get(url)
    _driver.find_element(By.ID, "firstname").send_keys("John")
    _driver.find_element(By.ID, "surname").send_keys("Pourdanis")
    _driver.find_element(By.ID, "age").send_keys("35")
    select = Select(_driver.find_element(By.ID, "country"))
    select.select_by_value("Greece")
    _driver.find_element(By.ID, "notes").send_keys("Those are test notes")
    _driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    surname_error_message = _driver.find_element(
        By.CSS_SELECTOR, '[name=surnamevalidation]').text
    assert surname_error_message == "Surname provided is too short"
