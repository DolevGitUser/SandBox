import pytest
from playwright.sync_api import sync_playwright
from pages.page_opener import PageOpener


# Set up re-use functions as fixtures
@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def navigate_to_account_creation(browser):
    google = PageOpener(browser)
    google.navigate_to("https://www.google.com/")
    google.click_element(locator_type='label', locator_value='כניסה')
    google.click_element('role', 'button', name='חשבון חדש')
    try:
        google.click_element('text', 'לשימוש שלי')
    except Exception as e:
        print(f"Optional step failed: {e}")
        pass
    return google


# Positive
def test_valid_inputs(navigate_to_account_creation):
    google = navigate_to_account_creation
    google.fill_input('label', 'Dolev', "שם פרטי")
    google.fill_input('label', 'Dabush', "שם משפחה")
    google.click_element('role', "button", name="הבא")
    google.click_element('text', 'מידע בסיסי', exact=True)
    google.click_element('role', "button", name="הבא")


# Negative Cases
def test_empty_firstname(navigate_to_account_creation):
    google = navigate_to_account_creation
    google.click_element('role', "button", name="הבא")
    first_name_err = google.click_element('text', 'יש להזין שם פרטי')
    assert first_name_err.is_visible(), "The element was not visible."


def test_empty_date(navigate_to_account_creation):
    google = navigate_to_account_creation
    google.fill_input('label', 'Dolev', "שם פרטי")
    google.fill_input('label', 'Dabush', "שם משפחה")
    google.click_element('role', "button", name="הבא")
    google.click_element('text', 'מידע בסיסי', exact=True)
    google.click_element('role', "button", name="הבא")
    b_day = google.click_element('text', "הזן תאריך לידה מלא")
    gender = google.click_element('text', "יש לבחור מגדר")
    assert b_day.is_visible(), "The element was not visible."
    assert gender.is_visible(), "The element was not visible."
