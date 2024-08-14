from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ImdbSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Replace with your desired webdriver path

    def search_by_name(self, first_name, last_name):
        url = f"https://www.imdb.com/search/name/"
        self.driver.get(url)

        # Find and fill in first name input (assuming ID "findName")
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "findName"))
        )
        first_name_input.send_keys(first_name)

        # Find and fill in last name input (assuming ID "findName")
        last_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "findName"))
        )
        last_name_input.send_keys(last_name + Keys.TAB)  # Send TAB to move to next field

        # Find and select from dropdown (assuming ID "tt")
        # Modify locator and selection logic based on actual IMDb implementation
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "tt"))
        )
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text.lower().startswith(last_name.lower()):  # Match first few characters
                option.click()
                break  # Exit loop after selecting

        # Find and click search button (assuming ID "find")
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "find"))
        )
        search_button.click()

    def quit(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    imdb_search = ImdbSearch()
    imdb_search.search_by_name("Tom", "Hanks")
    imdb_search.quit()  # Close the browser after the search
