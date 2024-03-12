# Browser Actions

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.amazon.com")
# sleep(2)
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# sleep(2)
# driver.close()

###################################################################################

# Resizing browser
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.myntra.com")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.minimize_window()
# sleep(2)
# driver.fullscreen_window()
# sleep(4)
# driver.close()

######################################################################################
# Getting window postion

# for size
# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.ajio.com")
# d=driver.get_window_size()
# # print(d)
# # print(d['width'])
# print(d['height'])
# driver.close()


# for position

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.ajio.com")
# d=driver.get_window_position()
# print(d)
# # print(d['x'])
# print(d['y'])
# driver.close()

# for rect

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.ajio.com")
# d=driver.get_window_rect()
# print(d)
# driver.close()

###########################################################################################################

# set window position

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.myntra.com")
# driver.set_window_size(12,56)


# position set

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.myntra.com")
# sleep(2)
# driver.set_window_position(92,-66)
# driver.close()

# rect set

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.myntra.com")
# sleep(2)
# driver.set_window_rect(4,5,23,67)
# driver.close()

#############################################################################################################

# verfication property

#for title

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.netflix.com")
# sleep(2)
# data=driver.title
# print(data)
# driver.close()


# for web url

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.netflix.com")
# sleep(2)
# data=driver.current_url
# print(data)
# driver.close()

# for page source

# from selenium.webdriver import Chrome
# from time import sleep
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https:/www.netflix.com")
# sleep(2)
# data=driver.page_source
# print(data)
# driver.close()
