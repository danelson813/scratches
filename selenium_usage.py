from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_url():
    return "https://www.redbox.com/showcase/most-popular"


def get_driver():
    url = get_url()
    options = Options()
    options.add_argument('--headless')
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent:{user_agent}')
    driver = webdriver.Firefox(
        service=Service('/Users/geckodriver'),
        options=options)
    driver.get(url)
    sleep(2)
    driver.maximize_window()
    driver.save_screenshot("homepage.png")
    browser = driver
    html = browser.page_source
    # soup = BeautifulSoup(browser.page_source, 'html.parser')
    driver.close()
    return html


def get_soup(html):
    return BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    get_driver()