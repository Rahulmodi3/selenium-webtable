from selenium.webdriver.common.by import By

from entity_row import EntityRow
from entity_cell import EntityCell


class EntityTable:

    def __init__(self, driver, parent_selector: str):
        """
           :param driver: webdriver
           :param parent_selector: web table parent css selector
        """

        self.driver = driver
        self.parent_selector = parent_selector

    def get_header_values(self) -> dict:
        """ Get table all headers name
                    """
        headers_selector = f"{self.parent_selector} thead th"
        headers_list = self.driver.find_elements(By.CSS_SELECTOR, headers_selector)
        headers_name = dict()

        for i in range(len(headers_list)):
            header = headers_list[i]
            header_value = header.get_attribute("textContent")  # if element is hidden then this will work
            if header_value:
                header_name = header_value.strip()
                headers_name[header_name] = i
        return headers_name

    def get_rows(self) -> list[EntityRow]:
        """ Get list of row elements
                            """
        rows = []
        headers_name = self.get_header_values()
        rows_elements = self.driver.find_elements(By.CSS_SELECTOR, f"{self.parent_selector} tbody tr")

        for item in rows_elements:
            rows.append(EntityRow(item, headers_name))
        return rows

    def get_row(self, column_name: str, searched_value: str) -> EntityRow | None:
        """ Get row element based on header name, and it's value

            :param column_name: provide table header name
            :param searched_value: value of provided header
        """

        row = None
        rows = self.get_rows()

        for r in rows:
            name_cell = r.get_table_cell(column_name)
            if name_cell:
                value = name_cell.get_cell_value()
                value.strip()
                if value == searched_value:
                    row = r
                    break
        return row

    def get_table_values(self) -> list[dict]:
        """ Get list of the whole table values
                            """
        result_table = []
        table_rows = self.get_rows()

        for row in table_rows:
            row_value = row.get_entity_row_values()
            result_table.append(row_value)
        return result_table

    def get_table_row_values(self, column_name: str, searched_value: str) -> dict:
        """ Get row values based on header name, and it's value

            :param column_name: provide table header name
            :param searched_value: value of provided header
                """
        row = self.get_row(column_name, searched_value)
        assert row is not None, f' value {searched_value} for column {column_name} not found.'
        return row.get_entity_row_values()

    def get_table_cell(self, column_name: str, searched_value: str) -> EntityCell:
        """ Get table cell based on header name, and it's value

            :param column_name: provide table header name
            :param searched_value: value of provided header
                        """
        row = self.get_row(column_name, searched_value)
        assert row != '', f' value {searched_value} for column {column_name} not found.'
        return row.get_table_cell(column_name)

    def get_table_column_value(self, column_name: str) -> list:
        """ Get list of the table column data
                            """
        result_table = []
        table_rows = self.get_rows()

        for row in table_rows:
            row_value = row.get_entity_row_values()
            result_table.append(row_value[column_name])
        return result_table
