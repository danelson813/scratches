# util_playwright.py

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def get_soup(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # page.fill('inpur#input-username', 'demo')
        # page.fill("input#input-password", 'demo')
        # page.click('button[type=submit]')
        page.is_visible('ol.row')
        html = page.inner_html('ol.row')
        soup = BeautifulSoup(html, 'html.parser')
        return soup
