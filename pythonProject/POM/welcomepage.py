class WelcomePage:
    def __init__(self,driver):
        self.driver=driver
    def register_link(self):
        self.driver.find_element("xpath","//a[.='Register']").click()
    def login_link(self):
        self.driver.find_element("xpath","//a[.='Log in']").click()