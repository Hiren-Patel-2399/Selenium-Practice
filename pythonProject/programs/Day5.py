from selenium.webdriver import Chrome
from time import sleep

driver=Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://www.zeptonow.com/")
driver.maximize_window()

driver.find_element("css selector","button[class=' py-1 px-7 text-base p7Nt5_ undefined border border-skin-primary !basis-1/2 py-1.5 !px-0.5 sm:!px-0 false false ']").click()
sleep(3)
driver.find_element("css selector","div[class='flex w-full lg:!max-w-4xl']").click()
sleep(2)
driver.find_element("css selector","input[class='QKusZQ bg-transparent KE5lYd text-sm md:text-base cursor-text']").send_keys("Fruits")
sleep(2)
driver.find_element("css selector",'a[href="/pn/dragon-fruit-imported/pvid/5c81bb1c-4eda-4ac6-9467-dbdd8d077796"]').click()
sleep(2)
driver.find_element("css selector","div[class='w-[4.9rem] sm:w-28 h-[2.215rem] sm:h-12 relative sm:my-11 block']").click()
driver.find_element("css selector","path[d='M12 4v16m8-8H4']").click()
driver.find_element("css selector","path[d='M12 4v16m8-8H4']").click()
driver.find_element("css selector","path[d='M12 4v16m8-8H4']").click()
driver.find_element("css selector","path[d='M12 4v16m8-8H4']").click()
sleep(2)
driver.find_element("css selector","a[href='/cart']").click()
sleep(2)
driver.find_element("css selector","h6[class='block font-lato _3FRewB   mTPYOF']").click()
sleep(1)
driver.find_element("css selector","input[class='QKusZQ bg-transparent KE5lYd']").send_keys(9876543210)
sleep(1)
driver.find_element("css selector","button[class=' py-1 px-7 text-base druz0x w-full border border-skin-primary E1uS1F false ']").click()
sleep(3)
driver.close()



