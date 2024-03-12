# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver import ChromeOptions
# #
# # ws to click on my vegetables in bigbasket and click on add to basket and click on login/sign-up
# # and enter mob and click on continue
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://bigbasket.com")
# driver.maximize_window()
# driver.find_element("xpath","(//div[contains(@class,'DeckImage___Styled')])[1]").click()
# ids=driver.window_handles
#
# for i in ids:
#     driver.switch_to.window(i)
#     if driver.title=="Buy Fresho Capsicum Green 1 Kg Online At Best Price of Rs 48 - bigbasket":
#         sleep(5)
#         driver.find_element("xpath", "(//button[.='Add to basket'])[1]").click()
#         driver.find_element("xpath","//button[.='Login/ Sign Up']").click()
#         sleep(2)
#         driver.find_element("xpath","//input[@id='multiform']").send_keys("9876543219")
#         driver.find_element("xpath","//button[@type='submit']").click()
#         break
#
# #################################################################################################################
#
# # 2. ws to upload a pdf file and click on download button and download in different folder
# op=ChromeOptions()
# op.add_experimental_option("prefs",{"safebrowsing.enabled":True,"download.default_directory": r"F:\Resumes"})
#
# driver=Chrome(executable_path="../drivers/chromedriver.exe", options=op)
# driver.get("https://smallpdf.com/pdf-to-word")
# driver.maximize_window()
# driver.find_element("xpath","//input[@type='file']").send_keys(r"F:\Resumes\Hiren Manual resume.pdf")
# sleep(10)
# driver.find_element("xpath","(//button[@type='submit'])[2]").click()
# sleep(10)
# driver.find_element("xpath","//span[.='Download']").click()
# #######################################################################
