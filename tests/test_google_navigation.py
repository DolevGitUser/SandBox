import pytest
from playwright.sync_api import sync_playwright
from pages.page_opener import PageOpener


@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_google_search(browser):
    google = PageOpener(browser)
    google.navigate_to("https://www.google.com/")
    google.click_element(locator_type='label', locator_value='כניסה')
    google.click_element('role', 'button', name='חשבון חדש')
    try:
        google.click_element('text', 'לשימוש שלי')
    except Exception as e:
        # Ignore if the element is not found
        print(e)
        pass
    google.click_element('role', "button", name="הבא")
    first_name_err = google.click_element('text', 'יש להזין שם פרטי')
    assert first_name_err.is_visible(), "The element was not visible."
    google.click_element(locator_type='label', locator_value='שם פרטי')
    google.fill_input('label','Dolev', "שם פרטי")
    google.click_element('role', "button", name="הבא")
    google.click_element('text', 'מידע בסיסי',exact=True)
    google.click_element('role', "button", name="הבא")
    b_day = google.click_element('text', "הזן תאריך לידה מלא")
    gender = google.click_element('text', "יש לבחור מגדר")
    assert b_day.is_visible(), "The element was not visible."
    assert gender.is_visible(), "The element was not visible."



