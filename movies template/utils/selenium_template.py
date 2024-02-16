# movies/utils/selenium_template

from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from pathlib import Path
import pandas as pd
from selenium.webdriver.common.by import By
import sqlite3


def get_soup(url_):
    path = Path("data/text_html.txt")
    if path.exists():
        with open(path, 'r') as f:
            text_ = f.read()
            soup = bs(text_, 'html.parser')
            print('run from file')
    else:
        options = Options()
        options.add_argument('--headless')
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f'user-agent:{user_agent}')
        with webdriver.Firefox(service=Service('/Users/geckodriver'), options=options) as driver:
            driver.get(url_)
            sleep(2)
            button = driver.find_element(By.CLASS_NAME, 'discovery__actions')
            button.click()
            sleep(2)
            button.click()
            sleep(2)
            button.click()
            driver.maximize_window()
            driver.save_screenshot("homepage.png")
            soup = bs(driver.page_source, 'html.parser')
            save_text(driver.page_source)
            print("run using selenium")
    
    return soup


def save_text(text_):
    path = 'data/text_html.txt'
    with open(path, 'w') as f:
        f.write(str(text_))

def form_dataframe(list_: list) -> bs:
    df = pd.DataFrame(list_)
    print(df.info())
    return df

def to_sqlite(df: pd.DataFrame) -> None:
    path = Path("data/movies.db")
    con = sqlite3.connect(path)
    df.to_sql("tomatoes", con, if_exists='replace', index=False)
    print(f"dataframe saved to {path}")

if __name__ == '__main__':
    print('wrong file run')
