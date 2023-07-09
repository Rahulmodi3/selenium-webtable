from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from entity_cell import EntityCell


class EntityRow:

    def __init__(self, row_element: WebElement, headers_name_mapping: dict):
        """
            :param row_element: row WebElement
            :param headers_name_mapping: dict of table header names
        """

        self.row_element = row_element
        self.headers_name_mapping = headers_name_mapping

    def get_table_cell(self, header_name: str) -> EntityCell:
        """ Get table cell based of header name

            :param header_name: give table header name
        """
        cell = None

        if self.headers_name_mapping.__contains__(header_name):
            cell_elements = self.row_element.find_elements(By.CSS_SELECTOR, 'td')
            cell_index = self.headers_name_mapping[header_name]

            if 0 <= cell_index <= len(cell_elements):
                cell = EntityCell(cell_elements[cell_index])

        return cell

    def get_entity_row_values(self) -> dict:
        """ Return row values

        """
        row_values = dict()

        for item in self.headers_name_mapping.keys():
            table_cell = self.get_table_cell(item)
            assert table_cell != '', f'table cell {item} is not available '
            actual_value = table_cell.get_cell_value()
            row_values[item] = actual_value

        return row_values
