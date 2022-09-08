from Generic.syncronization import _wait


class _Generic:
    def __init__(self, driver):
        self.driver = driver

    @_wait
    def enter_text(self, element, *, value):
        self.driver.find_element(*element).send_keys(value)

    @_wait
    def click_element(self, element):
        self.driver.find_element(*element).click()

    @_wait
    def get_title(self):
        self.driver.title
