from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

# ws to print all options in assending order from i am a DD from Gst--> New Register

# l=[]
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://reg.gst.gov.in/registration/")
# driver.maximize_window()
#
# a=driver.find_element("id","applnType")
# s=Select(a)
# options = s.options
# for i in options[1:]:
#     l.append(i.text)
# print(sorted(l))

# driver.close()

##################################################################################

#2 ws to create a dictionary of index and statemnet pair in states:

# d={}
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://reg.gst.gov.in/registration/")
# driver.maximize_window()
#
# states=driver.find_element("id","applnState")
#
# s=Select(states)
# options= s.options
# for i in options[1:]:
#     d[i.text]=options.index(i)
# print(d)
# driver.close()

###################################################################################

#3 ws to create a dict of first letter and list of states which starts with the same first letter

# d={}
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://reg.gst.gov.in/registration/")
# driver.maximize_window()
# sts=driver.find_element("id","applnState")
#
# s=Select(sts)
# options= s.options
# for i in options[1:]:
#     if (i.text[0]) not in d:
#         d[(i.text)[0]]=[i.text]
#     elif (i.text)[0] in d:
#         d[(i.text)[0]]+=[i.text]
# print(d)
#
# driver.close()

