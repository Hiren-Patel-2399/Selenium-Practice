from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.support.select import Select

driver=Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("http://student.mybmtc.com:8280/bmtc/login/secure")
driver.maximize_window()

stn = driver.find_element("xpath","//a[contains(.,'Up to 10th (State)')]")
stn.click()

cbse= driver.find_element("xpath","//a[contains(.,'CBSE/ICSE')]")
cbse.click()

puc = driver.find_element("xpath","//a[contains(.,'PUC')]")
puc.click()


ids=driver.window_handles
for i in ids:
    driver.switch_to.window(i)
    if driver.current_url== "http://student.mybmtc.com:8280/pass/anonymous/studentapplication/new/puc":
        driver.maximize_window()
        ssdd= driver.find_element("id","standard")
        s=Select(ssdd)
        s.select_by_value("1")

        rdobtn=driver.find_element("id","sat1")
        rdobtn.click()

        dob=driver.find_element("id","dob")
        dob.send_keys("05/02/2015")

        adhname=driver.find_element("id","nameAsPerAadhaar")
        adhname.send_keys("HirenRoshanPatel")

        # sat=driver.find_element("id","satNumber")
        # sat.send_keys("1244466")

        std=driver.find_element("id","applicantName")
        std.send_keys("HirenPatel")

        gnd=driver.find_element("id","applicantGender")
        s=Select(gnd)
        s.select_by_value("MALE")

        fname=driver.find_element("id","applicantFatherName")
        fname.send_keys("jhehgwed")

        m_name=driver.find_element("id","applicantMotherName")
        m_name.send_keys("wifjds")

        caste=driver.find_element("id","applicantCaste")
        s=Select(caste)
        s.select_by_value("GENERAL")

        # intname=driver.find_element("xpath","//input[@id='institution_name']")
        # intname.send_keys("BMS EVENING PU COLLAGE")

        # adress=driver.find_element("xpath","//textarea[@id='officeAddress']")
        # adress.send_keys("BTR, Basvanagudi")

        stu_add=driver.find_element("id","applicantAddress")
        stu_add.send_keys("Hanumanthnagar, Basvanagudi Banglore")

        pncd=driver.find_element("id","pincode")
        pncd.send_keys("560009")

        m_no=driver.find_element("id","mobileNo")
        m_no.send_keys("9876543219")

        adhar=driver.find_element("id","aadhaarNumber")
        adhar.send_keys("8765866388928266")

        fromadd=driver.find_element("id","fromStopName")
        fromadd.send_keys("Basavanagudi Police Station")

        toadd=driver.find_element("id","toStopName")
        toadd.send_keys("BMS College")

        btn=driver.find_element("xpath","(//input[@type='file'])[1]")
        btn.send_keys("C:\\Users\\hiren\\OneDrive\\Desktop\\Passport size photo")

        btn2=driver.find_element("xpath","(//input[@type='file'])[2]")
        btn2.send_keys("C:\\Users\\hiren\\OneDrive\\Desktop\\Passport size photo")

        opt=driver.find_element("xpath","(//button[@type='button'])[1]")
        opt.click()













        break



