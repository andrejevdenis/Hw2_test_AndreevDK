from selene import browser, be, have
import pytest

@pytest.fixture
def openbrowser():
    browser.open('https://google.com')
    browser.driver.set_window_size(1920, 1080)