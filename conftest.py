import secrets
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

randomEmail = f"{secrets.token_hex(8)}@mail.com"


class NewUser:
    id = None
    name = "John Pourdanis"
    email = randomEmail
    gender = "male"
    status = "active"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    url = "https://the-internet.herokuapp.com"
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=options)
    driver.get(url)
    yield driver
    driver.close()
