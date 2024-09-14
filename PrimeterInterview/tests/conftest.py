# Set up re-use functions as fixtures
import pytest
from playwright.sync_api import sync_playwright, expect
from PrimeterInterview.pages.page_interactor import PageInteractor


@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def navigate_to_account_creation(browser, url="https://www.google.com/?hl=en", sing_in_button='Sign in',
                                 crate_account='Create account', account_usage='For my personal use',
                                 create_account_page="Create a Google Account"):
    google_page = PageInteractor(browser)
    google_page.navigate_to(url)
    google_page.click_element(locator_type='label', locator_value=sing_in_button)
    google_page.click_element(locator_type='role', locator_value='button', name=crate_account)
    try:
        google_page.click_element(locator_type='text', locator_value=account_usage)
    except Exception as e:
        print(f"Optional step failed: {e}")
        pass
    expect(google_page.find_element(locator_type='text', locator_value=create_account_page))
    return google_page
