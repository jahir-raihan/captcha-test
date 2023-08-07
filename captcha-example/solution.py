from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
from time import sleep

url = 'https://www.google.com/recaptcha/api2/demo'

browser = Chrome()
browser.get(url)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'recaptcha-demo')))
site_key = browser.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = TwoCaptcha('f03499fd11615e8347f6aa29254be92d')  # -> API Key
result = solver.solve_captcha(site_key, url)    # Solving Recaptcha

print(result)
browser.execute_script(f'document.getElementById("g-recaptcha-response").value = "{result}"')   # Inserting result code

browser.find_element(By.XPATH, '//*[@id="recaptcha-demo-submit"]').click()  # Submitting form
sleep(50)
browser.close()