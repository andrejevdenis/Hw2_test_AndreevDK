from selene import browser, be, have
import pytest

@pytest.fixture
def serch1(openbrowser):
    browser.element('[name="q"]').should(be.blank).type('налог ру').press_enter()

def test_serch1(serch1):
    browser.element('[id="search"]').should(have.text('Федеральная налоговая служба'))

@pytest.fixture
def serch2(openbrowser):
    browser.element('[name="q"]').should(be.blank).type('|\|\|').press_enter()

def test_serch2(serch2):
    browser.element('[aria-level="3"]').should(have.text(' ничего не найдено.'))