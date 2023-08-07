from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


"""Initial Script for testing"""

chrome = Chrome()


chrome.get('https://www.whitepages.com/')
chrome.implicitly_wait(10)
name_input = chrome.find_element(By.XPATH, '//*[@id="search-name"]')
location_input = chrome.find_element(By.XPATH, '//*[@id="search-location"]')
submit_button = chrome.find_element(By.XPATH, '//*[@id="wp-search"]')

name_input.send_keys('Joy')
location_input.send_keys('New York')
submit_button.click()
chrome.implicitly_wait(10)

user_data = chrome.find_elements(By.CLASS_NAME, 'serp-card')[1]

user_data.click()

sleep(10)

path = chrome.current_url.split('/')
path_id = chrome.current_url.split('/')[-1]
print(path)
print(path_id)

name = chrome.find_element(By.XPATH, f'//*[@id="{path_id}"]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/h1').text.strip()

land_line = chrome.find_element(By.XPATH, '//*[@id="landline"]/div[2]/a').text.strip()

age = chrome.find_element(By.XPATH, f'//*[@id="{path_id}"]/div/div[1]/div[1]/'
                                    f'div[1]/div[1]/div[2]/div[2]/div[1]/div[2]').text.strip()

location = chrome.find_element(By.XPATH, f'//*[@id="{path_id}"]/div/div[1]/div[1]/'
                                         'div[1]/div[1]/div[2]/div[2]/div[2]/div[2]').text.strip()


print(name, land_line, age, location)


subject = 'Remove my data'
email = ''.join(name.split()).lower() + '@gmail.com'
description = 'Remove my data from the database'
listing_url = chrome.current_url

chrome.get('https://support.whitepages.com/hc/en-us/requests/new?ticket_form_id=580868')

sleep(5)

email_input = chrome.find_element(By.NAME, 'request[anonymous_requester_email]')
email_input.clear()
email_input.send_keys(email)
listing_url_input = chrome.find_element(By.NAME, 'request[custom_fields][44339788]')
listing_url_input.clear()
listing_url_input.send_keys(listing_url)

listing_name_email = chrome.find_element(By.NAME, 'request[custom_fields][360007194753]')
listing_name_email.clear()
listing_name_email.send_keys(name)

listing_address = chrome.find_element(By.NAME, 'request[custom_fields][360007272574]')
listing_address.clear()
listing_address.send_keys(location)

listing_phone_number = chrome.find_element(By.NAME, 'request[custom_fields][360007272554]')
listing_phone_number.clear()
listing_phone_number.send_keys(land_line)

reason_for_remove = chrome.find_elements(By.CLASS_NAME, 'nesty-input')
reason_for_remove[1].click()
actions = ActionChains(chrome)
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ENTER).perform()

subject_input = chrome.find_element(By.NAME, 'request[subject]')
subject_input.clear()
subject_input.send_keys(subject)

description_input = chrome.find_element(By.NAME, 'request[description]')
description_input.clear()
description_input.send_keys(description)

sleep(3)

submit = chrome.find_element(By.NAME, 'commit')

submit.click()

sleep(100)
chrome.close()

