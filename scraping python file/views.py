import time
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
def extract_phone_number(href):
    url = "https://www.whitepages.com" + href
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/phone/"]')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        phone_number = soup.select_one('a[href^="/phone/"]').text.strip()
        time.sleep(3)
        driver.quit()
        
        if phone_number=="Phone Numbers":
            return "No Number Were found"
        return phone_number
    except:
        time.sleep(3)
        driver.quit()
        return "No Number Were found"


def fill_form_and_submit(full_name, location, phone_number,href):
    url = "https://www.whitepages.com" + href
    if phone_number == "No Number Were found":
        phone_number= "202-555-0184"
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    try:
        driver.get("https://support.whitepages.com/hc/en-us/requests/new?ticket_form_id=580868")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'request[anonymous_requester_email]')))
        time.sleep(1)
        email_input = driver.find_element(By.NAME,'request[anonymous_requester_email]')
        email_input.clear()
        email_input.send_keys("full_name@email.com")
        time.sleep(1)
        listing_url_input = driver.find_element(By.NAME,'request[custom_fields][44339788]')
        listing_url_input.clear()
        listing_url_input.send_keys(url)  
        time.sleep(1)
        listing_name_email = driver.find_element(By.NAME,'request[custom_fields][360007194753]')
        listing_name_email.clear()
        listing_name_email.send_keys(full_name)  
        time.sleep(1)
        listing_address = driver.find_element(By.NAME,'request[custom_fields][360007272574]')
        listing_address.clear()
        listing_address.send_keys(location)  
        time.sleep(1)
        listing_phone_number = driver.find_element(By.NAME,'request[custom_fields][360007272554]')
        listing_phone_number.clear()
        listing_phone_number.send_keys(phone_number)          
        time.sleep(1)
        reason_for_remove =driver.find_elements(By.CLASS_NAME, 'nesty-input')
        reason_for_remove[1].click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        subject = driver.find_element(By.NAME,'request[subject]')
        subject.clear()
        subject.send_keys("Application for Remove")     
        time.sleep(1)
        description = driver.find_element(By.NAME,'request[description]')
        description.clear()
        description.send_keys("please remove my listing ")      
        time.sleep(2.5)
        submit = driver.find_element(By.NAME,'commit')
        submit.click()
        time.sleep(6)
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
    finally:
        driver.quit() 
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)
url = 'https://www.whitepages.com/name/Jhon/NY?fs=1&searchedName=jhon&searchedLocation=ny'
driver.get(url)
time.sleep(3)
html_content = driver.page_source
soup = BeautifulSoup(html_content, 'html.parser')
result_list = []
for a_tag in soup.select('a.serp-card'):
    age = a_tag.select_one('span.person-age').text.strip()
    full_name = a_tag.select_one('div.name-wrap > span').text.strip()
    location = a_tag.select_one('span.person-location-city').text.strip()
    href = a_tag['href'] 
    phone_number = extract_phone_number(href)
    result = {
        'age': age,
        'fullName': full_name,
        'location': location,
        'href': href,  
        'phone': phone_number,
    }
    fill_form_and_submit(full_name=full_name,location=location,phone_number=phone_number,href=href)
    result_list.append(result)
print(result_list)
