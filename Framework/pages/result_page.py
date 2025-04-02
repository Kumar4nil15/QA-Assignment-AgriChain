from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def get_result(self):
        return self.driver.find_element(By.ID, "result").text
