from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Generic import Cons


def _wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance, Cons.TIME_OUT)
        wait.until(expected_conditions.visibility_of_element_located(locator))
        return func(*args, **kwargs)

    return wrapper()
