# ws to check create account, full name and email is enable or not(click on signup)in zomato

from selenium.webdriver import Chrome
from time import sleep

# driver=Chrome(executable_path='../drivers/chromedriver.exe')
# driver.get('https://www.zomato.com/bangalore')
# driver.maximize_window()
#
# signup= driver.find_element("xpath","//a[.='Sign up']")
# signup.click()
#
# name= driver.find_element("xpath","(//input[@type='text'])[1]")
# print(name.is_enabled())
#
# email= driver.find_element("xpath","(//input[@type='text'])[2]")
# print(email.is_enabled())
#
# acc= driver.find_element("xpath","(//button[@role='button'])[2]")
# print(acc.is_enabled())
#
# driver.close()

##############################################################################################
#ws to check new registration and trn is selected or not

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://reg.gst.gov.in/registration")
# driver.maximize_window()
#
# rdo_name= driver.find_element("xpath","//input[@id='radionew']")
# sleep(1)
# print(rdo_name.is_selected())
#
# trn= driver.find_element("xpath","//input[@id='radiotrn']")
# print(trn.is_selected())
# driver.close()
###########################################################################################

#ws to check recruitmenet, rti ,tenders element is presentor not

driver=Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://cetonline.karnataka.gov.in/kea/dcet23")
driver.maximize_window()

req= driver.find_element("xpath","(//a[@class='home-text nav-link dropdown-toggle'])[3]")
print(req.is_displayed())

rti= driver.find_element("xpath","(//li[@class='nav-item'])[1]")
print(rti.is_displayed())

tenders= driver.find_element("xpath","(//li[@class='nav-item'])[2]")
print(tenders.is_displayed())

driver.close()

##################################################################################################

# ws to get loction, size, and rect  of kids in ajio

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com/")
# driver.maximize_window()
#
# kids= driver.find_element("xpath","//span[.='KIDS']")
# print(kids.location)
# print(kids.size)
# print(kids.rect)
# driver.close()

###########################################################################################

# ws to print text of python and then click --> print text of python variable and click -->
# print text of output variable and click --> print text of previous and click

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.w3schools.com/")
# driver.maximize_window()
#
# p_txt = driver.find_element("xpath","//a[.='PYTHON']")
# print(p_txt.text)
# print(p_txt.click())
#
# p_var= driver.find_element("xpath","(//a[.='Python Variables'])[1]")
# print(p_var.text)
# print(p_var.click())
#
# O_var= driver.find_element("xpath","//a[.='Output Variables']")
# print(O_var.text)
# print(O_var.click())
#
# pre = driver.find_element("xpath","(//a[.='❮ Previous'])[1]")
# print(pre.text)
# print(pre.click())
#
# sleep(3)
# driver.close()