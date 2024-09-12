class PageOpener:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        """
        Navigate to the given URL.
        """
        self.page.goto(url)

    def click_element(self, locator_type, locator_value=None, name=None, exact=False):
        """
        Perform a click action based on the type of locator and return the element clicked.
        Supported types: 'label', 'role', 'text'.
        """
        if locator_type == 'label':
            element = self.page.get_by_label(locator_value)
        elif locator_type == 'role':
            element = self.page.get_by_role(locator_value, name=name)
        elif locator_type == 'text':
            element = self.page.get_by_text(locator_value, exact=exact)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")
        element.click()
        return element

    def fill_input(self, locator_type, text, locator_value=None, name=None):
        """
        Fill an input field located by a given type with the provided text.
        Supported types: 'label', 'role', 'text'.
        """

        if locator_type == 'label':
            element = self.page.get_by_label(locator_value)
        elif locator_type == 'role':
            element = self.page.get_by_role(locator_value, name=name)
        elif locator_type == 'text':
            element = self.page.get_by_text(locator_value)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")
        element.fill(text)

