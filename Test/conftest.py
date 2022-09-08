from selenium.webdriver import Chrome
from Generic.Cons import URL
from pytest import fixture


@fixture
def setup():
    driver = Chrome()
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.close()
