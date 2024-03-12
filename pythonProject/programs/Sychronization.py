from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element("xpath","//a[.='Facebook']").click()
# ids = driver.window_handles
# driver.switch_to.window(ids[1])
# wait= WebDriverWait(driver, 10)
# wait.until(EC.title_is("NopCommerce | Facebook"))
# print("switch to title successfully")


# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element("xpath","//a[.='Facebook']").click()
# ids = driver.window_handles
# driver.switch_to.window(ids[1])
# wait= WebDriverWait(driver, 10)
# wait.until(EC.title_contains("Facebook"))
# print("switch to title successfully")

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element("xpath","//a[.='Facebook']").click()
# ids = driver.window_handles
# driver.switch_to.window(ids[1])
# wait= WebDriverWait(driver, 10)
# wait.until(EC.url_to_be("https://www.facebook.com/nopCommerce"))
# print("switch to title successfully")

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element("xpath","//a[.='Facebook']").click()
# ids = driver.window_handles
# driver.switch_to.window(ids[1])
# wait= WebDriverWait(driver, 10)
# wait.until(EC.url_contains("www.facebook.com"))
# print("switch to title successfully")

###########################################################################################
#Fluent wait

# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element("xpath","//a[.='Facebook']").click()
# ids = driver.window_handles
# driver.switch_to.window(ids[1])
# wait= WebDriverWait(driver, 10,poll_frequency=1)
# wait.until(EC.url_to_be("https://www.facebook.com/nopCommerce"))
# print("switch to title successfully")