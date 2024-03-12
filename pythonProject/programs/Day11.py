from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# driver= Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.ajio.com")
# driver.maximize_window()
#
# men=driver.find_element("xpath","//span[.='MEN']")
# sleep(2)
# a=ActionChains(driver)
# a.move_to_element(men).perform()
# wear=driver.find_elements("xpath","(//a[@href='/men-western-wear/c/830216'])[1]/../following-sibling::div")
#
# l=[]
# for i in wear:
#     l.append(i.text)
# print(l)
#
# driver.close()
#
# ###########################################################################

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.meesho.com/")
# driver.maximize_window()
#
# bags=driver.find_element("xpath","//span[.='Bags & Footwear']")
# a=ActionChains(driver)
# a.move_to_element(bags).perform()
#
# d={}
# all_bags=driver.find_elements("xpath","//div[contains(@class,'nav-sub-list nav-sub-list')]")
# for j in all_bags[28:33]:
#     l=j.text.split("\n")
#     d[l[0]]=l[1:]
# print(d)
#
# driver.close()

########################################################################################3
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.byjus.com/")
# driver.maximize_window()
#
# study=driver.find_element("xpath","//a[.='Study Materials']")
# a=ActionChains(driver)
# a.move_to_element(study).perform()
#
#
# ncrt= driver.find_element("xpath","(//a[.='NCERT Solutions'])[1]")
# a=ActionChains(driver)
# a.move_to_element(ncrt).perform()
#
# l=[]
# nrt=driver.find_elements("xpath","//li[@class='sub']/..")
# for i in nrt:
#     l.append(i.text)
# print(l)
#
# classes= driver.find_element("xpath","//a[.='Classes']")
# a=ActionChains(driver)
# a.move_to_element(classes).perform()
#
# l1=[]
# cls=driver.find_elements("xpath","//ul[@class='right-popopen']")
#
# for i in cls:
#     l1.append(i.text)
# print(l1)
#
# cbse= driver.find_element("xpath","(//a[.='CBSE'])[1]")
# a=ActionChains(driver)
# a.move_to_element(cbse).perform()
#
# l2=[]
# cse=driver.find_elements("xpath","(//li[@class='sub']/..)[3]")
#
# for i in cse:
#     l2.append(i.text)
# print(l2)
#
# driver.close()