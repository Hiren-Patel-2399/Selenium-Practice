import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

@pytest.mark.parametrize("name,mobileno,email,state",[['hiren','9876543210','abc@gmail.com','select',],
                                                      ['neel','9553718312','qbd@gmail.com','select'],
                                                      ['bhavu','9458287654','bhavu@gmail.com','select']])
def test_Byjus(name,mobileno,email,state):
    driver=Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://byjus.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element("xpath","(//input[@type='text'])[1]").send_keys(name)
    driver.find_element("xpath","(//input[@type='text'])[2]").send_keys(mobileno)
    driver.find_element("xpath","//input[@type='email']").send_keys(email)
    a=driver.find_element("xpath","//select[@name='state']")
    s=Select(a)
    s.select_by_value("Chhattisgarh")
    driver.find_element("xpath","//button[.='Continue to Schedule']").click()

