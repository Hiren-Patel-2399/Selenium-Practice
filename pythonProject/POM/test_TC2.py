from welcomepage import *
from loginpage import *

def test_TC2(launch):
    driver=launch
    w = WelcomePage(driver)
    w.login_link()
    l= LoginPage(driver)
    l.email("selenium@gmail.com")
    l.password("selenium@123")
    l.login_button()