import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("first_name, last_name, expected_result", [
    ("Dolev", "Dabush", "Basic information"),  # Positive case: valid inputs
    ("", "Dabush", "Enter first name"),  # Negative case: missing first name
    ("Dolev", "", "Basic information")  # Negative case: missing last name
])
def test_name_fields(navigate_to_account_creation, first_name, last_name, expected_result, next_button="Next"):
    """
    Test the First name and Last name fields during Google account creation.
    Test Cases:
        - If the first name is empty, it checks for the presence of an error message.
        - If a valid name is provided, it checks for the success message or behavior.
    """
    google_page = navigate_to_account_creation
    google_page.fill_input(locator_type='label', locator_value="First name", text=first_name)
    google_page.fill_input(locator_type='label', locator_value="Last name", text=last_name)
    google_page.click_element(locator_type='role', locator_value="button", name=next_button)
    if first_name == "":
        expect(google_page.find_element(locator_type='locator', locator_value="#nameError")).to_contain_text(
            expected_result)
    else:
        expect(google_page.find_element(locator_type='text', locator_value=expected_result, exact=True)).to_be_visible()


@pytest.mark.parametrize("day, month_option, year, gender_option, expected_result", [
    ("01", "1", "1996", "1", "Choose your Gmail address"),  # Positive case: valid date and gender
    ("", "1", "1996", "1", "#dateError"),  # Negative case: missing day
    ("01", "1", "", "1", "#dateError"),  # Negative case: missing year
    ("01", "1", "1996", "", "#genderError")  # Negative case: missing gender
])
def test_date_and_gender_fields(navigate_to_account_creation, day, month_option, year, gender_option, expected_result,
                                next_button="Next"):
    """
    Test the Date of Birth and Gender fields during Google account creation.
    Test Cases:
        - Verifies that when valid date and gender values are entered, the correct
          confirmation message appears.
        - Checks for validation errors when required fields (day, year, or gender)
          are missing.
    """
    google_page = navigate_to_account_creation
    google_page.fill_input(locator_type='label', locator_value="First name", text="Dolev")
    google_page.fill_input(locator_type='label', locator_value="Last name", text="Dabush")
    google_page.click_element(locator_type='role', locator_value="button", name=next_button)
    expect(google_page.find_element(locator_type='text', locator_value="Basic information", exact=True)).to_be_visible()
    google_page.select_element(locator_type='label', locator_value="Month", option=month_option)
    google_page.fill_input(locator_type='label', locator_value="Day", text=day)
    google_page.fill_input(locator_type='label', locator_value="Year", text=year)
    google_page.select_element(locator_type='locator', locator_value="xpath=//*[@id='gender']", option=gender_option)
    google_page.click_element(locator_type='role', locator_value="button", name=next_button)
    if expected_result.startswith("#"):
        expect(google_page.find_element(locator_type='locator', locator_value=expected_result)).to_be_visible()
    else:
        expect(google_page.find_element(locator_type='text', locator_value=expected_result, exact=True)).to_be_visible()
