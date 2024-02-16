from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from .util import setup_logger, does_it_exist
import pandas as pd



def get_soup(url_):
    logger = setup_logger()
    options = Options()
    options.add_argument('--headless')
    ua = UserAgent()
    user_agent = ua.random
    # logger.info(f"{user_agent}")
    options.add_argument(f'user-agent:{user_agent}')
    with webdriver.Firefox(service=Service('/Users/geckodriver'), options=options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("data/homepage.png")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        return soup
    
def save_soup(soup):
    with open('data/html_for_soup.txt', 'w') as f:
        f.write(soup)

def retreive_soup(filename):
    with open(filename, 'r') as f:
        text = f.read()
        return BeautifulSoup(text, 'html.parser')

def obtain_soup():
    logger = setup_logger()
    url = "https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaLQCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuAKCtO2sBsACAdICJGQ5YzRkMjZkLWY0Y2YtNDNhNC05MDkxLTVmY2E5NmU3OWU2MNgCBeACAQ&sid=1b32a53bf9957e29791ed0e41915c5bb&checkin_monthday=29&checkin_year_month=2024-01&checkout_monthday=31&checkout_year_month=2024-01&dest_id=20144123&dest_type=city&from_history=1&group_adults=2&no_rooms=1&order=popularity&sb_travel_purpose=leisure&si=ad&si=ai&si=ci&si=co&si=di&si=la&si=re&sh_position=1&auth_success=1"
    
    filename = "data/html_for_soup.txt"

    if does_it_exist(filename):
        soup = retreive_soup(filename=filename)
        logger.info("Used the file")
    else:
        logger.info("Used selenium")
        soup = get_soup(url)
        save_soup(str(soup))
    return soup


if __name__ == '__main__':
    print("You have run the wrong file")