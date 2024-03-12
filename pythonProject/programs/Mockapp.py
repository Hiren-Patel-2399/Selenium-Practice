# from selenium.webdriver import Chrome
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
#
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://www.swiggy.com/")
# driver.maximize_window()
#
# driver.find_element("xpath","//a[.='Search']").click()
# sleep(3)
#
# serach= driver.find_element("xpath","//input[@type='text']")
# serach.send_keys("Sandwish")
# sleep(2)
#
#
#
# pduct= driver.find_element("xpath","(//button[@data-testid='autosuggest-item'])[1]")
# pduct.click()
# sleep(5)
#
# allitems=driver.find_elements("xpath","//div[contains(@class,'styles_restaurantName')]")
#
# for i in allitems:
#     print(i.text)
# # l=[]
# # for i in allitems:
# #     l.append(i.text)
# # print(l)
# add= driver.find_element("xpath","(//div[@class='_1RPOp'])[1]")
# add.click()
# sleep(2)
#
# # additem=driver.find_element("xpath","//span[@class='_38xdN']")
# # additem.click()
#
# cart=driver.find_element("xpath","//span[.='Cart']")
# cart.click()
#
# sleep(2)
# signin= driver.find_element("xpath","//div[@class='OsNTr y9pNN']")
# signin.click()
#
# phno= driver.find_element("id","mobile")
# phno.send_keys("9876543212")
#
# name= driver.find_element("xpath","//input[@type='text']")
# name.send_keys("Hiren")
#
# email= driver.find_element("xpath","//input[@type='email']")
# email.send_keys("hrn@gmail.com")
#
# sleep(3)
# submit= driver.find_element("xpath","//a[.='CONTINUE']")
# submit.click()
#
#
# sleep(5)
# driver.close()
