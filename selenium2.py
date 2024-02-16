# import selenium



geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title

def get_driver():
    service = Service()
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(10)
    return driver

