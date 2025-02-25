from selenium import webdriver

class DriverManager:
    def __init__(self):
        self.driver = None


    def get_driver(self):
        return self.driver

    def start_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver
    


    def quit_driver(self):
        if self.driver:
            self.driver.quit()
