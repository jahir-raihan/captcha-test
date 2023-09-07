from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def main():
    chrome_options = webdriver.ChromeOptions()
    ip = 'yjixarcq:2y4mfkttnrmi@172.245.7.2:5055'

    chrome_options.add_argument(f'--proxy-server={ip}')

    url = 'https://whatismyipaddress.com'
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)

    sleep(10)

main()