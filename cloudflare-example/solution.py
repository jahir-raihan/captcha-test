from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


"""Final Script"""


class RequestDeletion:

    def __init__(self):
        self.browser = Chrome()
        self.collected_data = []

    def wait(self, selector, element):

        """Waits for a html dynamic element to be loaded, maximum wait time is 10sec"""

        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((selector, element)))
        except:
            print("Took too much time to load.")

    def search_and_execute(self, name, location):

        """Searches for a person, using name and location on whitepages website"""

        # Opening browser
        self.browser.get('https://www.whitepages.com/')

        # Finding input areas
        name_input = self.browser.find_element(By.XPATH, '//*[@id="search-name"]')
        location_input = self.browser.find_element(By.XPATH, '//*[@id="search-location"]')
        submit_button = self.browser.find_element(By.XPATH, '//*[@id="wp-search"]')

        # Inserting name and location in those input areas
        name_input.send_keys(name)
        location_input.send_keys(location)

        
        submit_button.click()
        sleep(5)

        # Crawl method to crawl over returned response
        self.crawl_data()

    def crawl_data(self):

        """Method to crawl and scrape over all query result after search"""

        user_datas = self.browser.find_elements(By.CLASS_NAME, 'serp-card')
        i = 0
        visited = []

        # Loop until we visit all similar persons data
        while i < len(user_datas):

            try:
                if user_datas[i].get_attribute('href') not in visited:   # Duplicate check
                    visited.append(user_datas[i].get_attribute('href'))

                    # Navigate to current person details page
                    user_datas[i].click()
                    sleep(3)

                    # Extract data using extract method
                    self.extract_data()

                    # Backs browser navigation history by 1 step
                    self.browser.back()
                    self.browser.refresh()
                    sleep(3)
                    user_datas = self.browser.find_elements(By.CLASS_NAME, 'serp-card')

            except:
                break

            i += 1
        print("counter end, i is", i)
        sleep(50)   # waits 50s before closing window.
        self.browser.close()

    def extract_data(self):

        """Extracts Name, age, Address, Land-Line of a person and sends for removal request"""

        path_id = self.browser.current_url.split('/')[-1]

        # Extracting Name, land_line/phone, age and address
        name = self.browser.find_element(By.XPATH, f'//*[@id="{path_id}"]/div/div[1]/div[1]/'
                                         f'div[1]/div[1]/div[1]/div/div/h1').text.strip()

        try:
            land_line = self.browser.find_element(By.XPATH, '//*[@id="landline"]/div[2]/a').text.strip()
        except:
            land_line = '(585) 589-5719'

        age = self.browser.find_element(By.XPATH, f'//*[@id="{path_id}"]/div/div[1]/div[1]/'
                                                  f'div[1]/div[1]/div[2]/div[2]/div[1]/div[2]').text.strip()

        location = self.browser.find_element(By.XPATH, f'//*[@id="{path_id}"]/div/div[1]/div[1]/'
                                                       'div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text.strip()

        data = {'name': name, 'phone': land_line, 'age': age, 'location': location, 'url': self.browser.current_url}

        self.collected_data.append(data)

        # Performing removal request for current person data
        self.submit_data(data)

        # Backs browser navigation history by 1 step
        self.browser.back()

    def submit_data(self, data):

        """Searches input areas for removal request form, and submits the data.
            After success, browser gets back to its original position. Eg: Returns to crawl_data method state."""

        email = ''.join(data['name'].split()).lower() + '@gmail.com'

        # Opening support page form
        self.browser.get('https://support.whitepages.com/hc/en-us/requests/new?ticket_form_id=580868')
        self.wait(By.NAME, 'request[anonymous_requester_email]')
        sleep(2)

        # Searching input areas and inserting inputs
        email_input = self.browser.find_element(By.NAME, 'request[anonymous_requester_email]')
        email_input.clear()
        email_input.send_keys(email)
        listing_url_input = self.browser.find_element(By.NAME, 'request[custom_fields][44339788]')
        listing_url_input.clear()
        listing_url_input.send_keys(data['url'])

        listing_name_email = self.browser.find_element(By.NAME, 'request[custom_fields][360007194753]')
        listing_name_email.clear()
        listing_name_email.send_keys(data['name'])

        listing_address = self.browser.find_element(By.NAME, 'request[custom_fields][360007272574]')
        listing_address.clear()
        listing_address.send_keys(data['location'])

        listing_phone_number = self.browser.find_element(By.NAME, 'request[custom_fields][360007272554]')
        listing_phone_number.clear()
        listing_phone_number.send_keys(data['phone'])

        print(".")

        reason_for_remove = self.browser.find_element(By.XPATH, '//*[@id="new_request"]/div[8]/a')
        reason_for_remove.click()
        sleep(1)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()

        print('.')

        subject_input = self.browser.find_element(By.NAME, 'request[subject]')
        subject_input.clear()
        subject_input.send_keys('Request to remove my data')

        description_input = self.browser.find_element(By.NAME, 'request[description]')
        description_input.clear()
        description_input.send_keys('Please remove my data')

        sleep(1)

        # Submitting removal request
        submit = self.browser.find_element(By.NAME, 'commit')
        submit.click()

        print('Successfully submitted data for : ', data)

        sleep(2)

        # Backs browser navigation history by 1 step
        self.browser.back()


if __name__ == '__main__':

    request = RequestDeletion()
    request.search_and_execute('Joy', 'New York')
