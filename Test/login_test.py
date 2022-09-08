from POM import login_pom
from Data.xlrd_read import read_header, read_data
from pytest import mark

hedar = read_header("sheet1", "test_case_name")
data = read_data("sheet1", "test_case_name")


@mark.parametrize(hedar, data)
def login_test(setup, user_name, password):
    lp = login_pom(setup)
    lp.login_user_name(user_name)
    lp.login_password(password)
    lp.login_click()
    title = lp.get_title()
    assert title == ""
