# for demoshop tricentis

"""
from selenium.webdriver import Chrome
from time import sleep

driver=Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
sleep(1)
driver.find_element("id","gender-male").click()
driver.find_element("id","FirstName").send_keys("Hiren")
driver.find_element("id","LastName").send_keys("Patel")
driver.find_element("id","Email").send_keys("hiren123@gmail.com")
driver.find_element("id","Password").send_keys("hiren123@")
driver.find_element("id","ConfirmPassword").send_keys("hiren123@")
driver.find_element("id","register-button").click()
sleep(2)
driver.close()
"""


################################################################################################

# for ksrtc


# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ksrtc.in/oprs-web/login/show.do")
# driver.maximize_window()
# sleep(1)
# driver.find_element("id","userName").send_keys("hiren123@gmail.com")
# driver.find_element("id","password").send_keys("hiren123@_")
# # driver.find_element("id","TermsConditions").click()
# driver.find_element("id","submitBtn").click()
# sleep(2)
# driver.close()


###############################################################################################

from selenium.webdriver import Chrome
from time import sleep
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request_locale=en")
# driver.maximize_window()
# rdo_btn=driver.find_element("id","cpvLocationPO")
# rdo_btn.click()
# driver.find_element("id","givenName").send_keys("Hiren")
# driver.find_element("id","surname").send_keys("Patel")
# driver.find_element("id","email").send_keys("hiren@gmail.com")
# driver.find_element("id","emailloginSameno").click()
# driver.find_element("id","loginId").send_keys("hiren@123")
# driver.find_element("id","pwd").send_keys("hiren@12_")
# driver.find_element("id","confirmPwd").send_keys("hiren@12_")
# driver.find_element("id","hintAns").send_keys("Navsari")
# driver.find_element("id","frmSample_register").click()
# sleep(2)
# driver.close()

###############################################################################################

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.google.com/")
# driver.maximize_window()
# voice=driver.find_element("xpath","//div[@class='XDyW0e']")
# data=voice.get_attribute("aria-label")
# camera=driver.find_element("xpath","//div[@class='nDcEnd']")
# data2=camera.get_attribute("aria-label")
# print(data)     Search by voice
# print(data2)    Search by image