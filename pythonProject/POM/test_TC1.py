from welcomepage import *
from registerpage import *

def test_TC1(launch):
    driver=launch
    w= WelcomePage(driver)
    w.register_link()
    r = RegisterPage(driver)
    r.gender_male()
    r.first_name("selenium")
    r.last_name("automation")
    r.email("selenium@gmail.com")
    r.password("selenium@123")
    r.confrim_password("selenium@123")
    r.register_button()