from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.selenium_manager import SeleniumManager
from entity_table import EntityTable

chrome_option = webdriver.ChromeOptions()
chrome_option.set_capability("browserName", "chrome")
chrome_option.add_argument("--incognito")
SeleniumManager().driver_location(chrome_option)
driver = webdriver.Chrome(options=chrome_option)

""" Example 1 : click on checkbox if checkbox column have header name """


def click_checkbox_with_column_name():
    url = "https://testautomationpractice.blogspot.com/"

    # selector
    parent_table_css_selector = "table#productTable"

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    table = EntityTable(driver, parent_table_css_selector)

    # get the row element
    row_element = table.get_row("Name", "Product 4")
    # get table cell
    table_cell = row_element.get_table_cell("Select")
    # click on cell
    table_cell.click_cell()


""" Example 2 : click on button if button column have header name """


def click_button_with_column_name():
    url = "https://admin-demo.nopcommerce.com/Admin/Customer/List"

    # selector
    btn_login = "//button[text()='Log in']"
    parent_table_css_selector = "table#customers-grid"

    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, btn_login).click()
    driver.implicitly_wait(10)

    table = EntityTable(driver, parent_table_css_selector)

    """ if you want to edit customer from table"""
    # get the row element
    row_element = table.get_row("Name", "John Smith")
    # get table cell
    table_cell = row_element.get_table_cell("Edit")
    # click on cell
    table_cell.click_cell()


""" Example 3 : click on checkbox if checkbox column doesn't have header name """


def click_checkbox_without_column_name():
    url = "https://admin-demo.nopcommerce.com/Admin/Customer/List"

    # selector
    btn_login = "//button[text()='Log in']"
    parent_table_css_selector = "table#customers-grid"

    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, btn_login).click()
    driver.implicitly_wait(10)

    table = EntityTable(driver, parent_table_css_selector)

    """ if you want to edit customer from table"""
    # get the row element
    row = table.get_row("Name", "John Smith")
    # find checkbox of table row
    cell_element = row.row_element.find_element(By.CSS_SELECTOR, "td input[type='checkbox']")
    cell_element.click()

