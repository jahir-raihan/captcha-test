from undetected_chromedriver import Chrome
from seleniumwire import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Task:

    def __init__(self, search_keyword, driver_path):
        print('waiting')
        self.browser = webdriver.Chrome()  # driver_executable_path=driver_path
        self.datas = []
        self.keyword = search_keyword

    def execute(self):

        """Main executive method to execute automation process."""

        # Exception handling if the website doesn't behave as it should be
        try:
            self.browser.get('https://amazon.co.uk')
            self.search_data()
            self.browser.close()
        except:
            self.browser.close()
            self.execute()
            return

    def search_data(self):

        """Selects Fashion from department dropdown, and searches by search_keyword(optional)."""
        sleep(3)

        self.browser.find_element(By.XPATH, '//*[@id="searchDropdownBox"]').click()  # Dropdown
        self.browser.find_element(By.XPATH, '//*[@id="searchDropdownBox"]/option[19]').click()  # Fashion

        # Insert search_keyword and click search button

        __search_input = self.browser.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
        __search_input.clear()
        __search_input.send_keys(self.keyword)
        __search_button = self.browser.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
        __search_button.click()

        sleep(5)

        # Scrape datas and save them in a csv file
        self.scrape_and_save()

    def scrape_and_save(self):

        """Scrapes products titles and saves them into a csv file."""

        # Selecting all product titles of the current page
        self.datas = self.browser.find_elements(By.CLASS_NAME, 'a-size-base-plus')

        # Creating a new file data.csv and appending titles line by line
        with open('data.csv', 'w+') as f:
            f.writelines('product_title \n')
            for data in self.datas:
                f.writelines(data.text + '\n')
            f.close()


# Path should be this by default: '/usr/local/bin/chromedriver'
# Using this only because of error.
path_to_driver = '/Users/apple/Downloads/chromedriver-mac-x64/chromedriver'

# Execute operation
if __name__ == '__main__':
    automator = Task('shirt', path_to_driver)
    automator.execute()
