class PageInteractor:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        """
        Navigate to the given URL.
        """
        self.page.goto(url)

    def find_element(self, locator_type, locator_value=None, name=None, exact=False):
        """
        Find an element based on locator type.
        Supported types: 'label', 'role', 'text'.
        Returns the element.
        """
        if locator_type == 'label':
            return self.page.get_by_label(locator_value)
        elif locator_type == 'role':
            return self.page.get_by_role(locator_value, name=name)
        elif locator_type == 'text':
            return self.page.get_by_text(locator_value, exact=exact)
        elif locator_type == 'locator':
            return self.page.locator(locator_value)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

    def click_element(self, locator_type, locator_value=None, name=None, exact=False):
        """
        Click an element located by the provided locator type.
        """
        element = self.find_element(locator_type, locator_value, name, exact)
        element.wait_for(state="visible")
        element.click()
        return element

    def fill_input(self, locator_type, text, locator_value=None, name=None, exact=False):
        """
        Fill an input field located by the provided locator type.
        """
        element = self.find_element(locator_type, locator_value, name, exact)
        element.wait_for(state="visible")
        element.fill(text)
        return element

    def select_element(self, locator_type, option, locator_value=None, name=None, exact=False):
        """
        Fill an input field located by the provided locator type.
        """
        element = self.find_element(locator_type, locator_value, name, exact)
        element.wait_for(state="visible")
        element.select_option(option)
        return element



