from selene import browser, be, have
import pytest

@pytest.fixture
def serch_page(openbrowser):
    browser.element('[name="q"]').should(be.blank).type('налог ру').press_enter()
    browser.element('[id="search"]').should(have.text('Федеральная налоговая служба'))

@pytest.fixture
def result(serch_page):
    return serch_page

def test_serch(serch_page, result):

    assert result == "Федеральная налоговая служба"