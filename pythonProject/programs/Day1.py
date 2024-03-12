# Chrome browser

from selenium.webdriver import Chrome
from time import sleep
# absoult path
# driver=Chrome(executable_path=r"C:\Users\hiren\PycharmProjects\QSP_Selenium_Pratice\pythonProject\drivers\chromedriver.exe")
# sleep(2)
# driver.get("https://www.instagram.com")
# sleep(2)
# driver.close()
# relative path
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# sleep(2)
# driver.get("https://www.instagram.com")
# sleep(2)
# driver.close()

##################################################################################
# firefox browser

from selenium.webdriver import Firefox
from time import sleep

#  absolute path
# driver=Firefox(executable_path=r"C:\Users\hiren\PycharmProjects\QSP_Selenium_Pratice\pythonProject\drivers\geckodriver.exe")
# sleep(3)
# driver.get("https:/www.amazon.com")
# sleep(3)
# driver.close()

# relative path
# driver=Firefox(executable_path="../drivers/geckodriver.exe")
# sleep(3)
# driver.get("https:/www.amazon.com")
# sleep(3)
# driver.close()

###########################################################################################

# Edge browser

from selenium.webdriver import Edge
from time import sleep

# absolute path

# driver=Edge(executable_path=r"C:\Users\hiren\PycharmProjects\QSP_Selenium_Pratice\pythonProject\drivers\msedgedriver.exe")
# sleep(2)
# driver.get("https:/www.myntra.com")
# sleep(2)
# driver.close()

#relative path

# driver=Edge(executable_path="../drivers/msedgedriver.exe")
# sleep(2)
# driver.get("https:/www.myntra.com")
# sleep(2)
# driver.close()