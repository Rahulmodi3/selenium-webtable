from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement


class EntityCell:

    def __init__(self, table_cell_element: WebElement):
        """
            :param table_cell_element: table cell WebElement
        """
        self.table_cell_element = table_cell_element

    def get_cell_value(self):
        """ Get table cell text
                    """
        value = self.table_cell_element.text
        return value

    def click_cell(self):
        """ Click on table cell
                    """
        clickable_element: WebElement = self.get_click_element((By.TAG_NAME, "a"))

        if clickable_element is None:
            clickable_element = self.get_click_element((By.TAG_NAME, "button"))
        if clickable_element is None:
            clickable_element = self.get_click_element((By.CSS_SELECTOR, "input[type='radio']"))
        if clickable_element is None:
            clickable_element = self.get_click_element((By.CSS_SELECTOR, "input[type='checkbox']"))
        assert clickable_element is not None, "clickable_element is not found"

        clickable_element.click()

    def get_click_element(self, by_locator: tuple) -> WebElement | None:
        element: WebElement

        try:
            element = self.table_cell_element.find_element(*by_locator)
        except NoSuchElementException:
            element = None

        return element
