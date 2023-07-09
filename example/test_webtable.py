from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from entity_table import EntityTable

chrome_option = webdriver.ChromeOptions()
chrome_option.set_capability("browserName", "chrome")
chrome_option.add_argument("--incognito")
SeleniumManager().driver_location(chrome_option)

driver = webdriver.Chrome(options=chrome_option)
url = "http://the-internet.herokuapp.com/tables"

# selector
parent_table_css_selector = "table#table1"

driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

table = EntityTable(driver, parent_table_css_selector)

table_headers_names = table.get_header_values()
print("Table headers name: ", table_headers_names)

rows = table.get_rows()
print("Total rows in table: ", len(rows))
print("Total columns in table: ", len(table_headers_names))

table_row_values = table.get_table_row_values("First Name", "John")
print("Table specific row data: ", table_row_values)

table_column_values = table.get_table_column_value("First Name")
print("Specific Column data: ", table_column_values)

table_whole_values = table.get_table_values()
print("All table data: ", table_whole_values)
