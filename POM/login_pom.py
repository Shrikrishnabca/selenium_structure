from Generic.Base_class import _Generic
from Data.xlrd_read import read_locators


class Login(_Generic):
    locator = read_locators("sheet1")

    def __int__(self, driver):
        super.__init__(driver)

    def login_user_name(self, value):
        element = Login.locator[""]
        self.enter_text(element, value=value)

    def login_password(self, value):
        element = Login.locator[""]
        self.enter_text(element, value=value)

    def login_click(self):
        element = Login.locator[""]
        self.click_element(element)
