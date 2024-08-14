from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class IMDbSearchAutomation:
    def __init__(self):
        # Setup Chrome WebDriver with options
        self.options = Options()
        self.options.add_argument("--start-maximized")  # Start maximized (optional)
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        try:
            self.driver.get(url)
            print("Page opened successfully.")
        except Exception as e:
            print(f"Failed to open page: {str(e)}")

    def fill_form(self, name=None, birth_year=None, gender=None, starmeter_min=None, starmeter_max=None, job_category=None):
        try:
            if name:
                name_field = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
                name_field.send_keys(name)

            if birth_year:
                birth_year_field = self.wait.until(EC.presence_of_element_located((By.ID, "birth_date")))
                birth_year_field.send_keys(birth_year)

            if gender:
                gender_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "gender")))
                gender_dropdown.send_keys(gender)

            if starmeter_min:
                starmeter_min_field = self.wait.until(EC.presence_of_element_located((By.ID, "starmeter-min")))
                starmeter_min_field.send_keys(starmeter_min)

            if starmeter_max:
                starmeter_max_field = self.wait.until(EC.presence_of_element_located((By.ID, "starmeter-max")))
                starmeter_max_field.send_keys(starmeter_max)

            if job_category:
                job_category_field = self.wait.until(EC.presence_of_element_located((By.ID, "job-category")))
                job_category_field.send_keys(job_category)

            print("Form filled successfully.")

        except Exception as e:
            print(f"Error while filling the form: {str(e)}")

    def perform_search(self):
        try:
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
            search_button.click()

            # Wait for the search results page to load (example: waiting for result stats element)
            results_stats = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
            print("Search completed!")

        except Exception as e:
            print(f"Error during search: {str(e)}")

    def close_browser(self):
        try:
            self.driver.quit()
            print("Browser closed successfully.")
        except Exception as e:
            print(f"Error closing the browser: {str(e)}")


# Usage example:
if __name__ == "__main__":
    imdb_bot = IMDbSearchAutomation()
    imdb_bot.open_page("https://www.imdb.com/search/name/")
    imdb_bot.fill_form(
        name="Leonardo DiCaprio",
        birth_year="1974",
        gender="Male",
        starmeter_min="1000",
        starmeter_max="5000",
        job_category="Actor"
    )
    imdb_bot.perform_search()
    imdb_bot.close_browser()
