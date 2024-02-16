from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs


def get_soup_pw(url):
    with sync_playwright() as p:
        visible = "ol.row"
        browser =p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(url)
        # may not be needed
        # page.fill('input#input-username','demo')
        # page.fill('input#input-password','demo')
        # page.click('button[type=submit]')

        page.is_visible(visible)
        html = page.inner_html(visible)   #  selector which contains the info we want
        soup = bs(html, 'html.parser')
        
        return soup