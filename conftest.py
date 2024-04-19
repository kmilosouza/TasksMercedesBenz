import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

DEFAULT_DRIVER_IMPLICIT_WAIT = 30


@pytest.fixture()
def setup_teardown(request):
    url = "https://shop.mercedes-benz.com/en-au/shop/vehicle/srp/demo"
    global driver
    options = Options()
    options.add_argument('--headless=new')
    browser = "chrome"
    if browser == "chrome":
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(DEFAULT_DRIVER_IMPLICIT_WAIT)
    yield driver
    driver.close()
