from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_string(self, input_text):
        self.driver.find_element(By.ID, "inputField").send_keys(input_text)

    def click_submit(self):
        self.driver.find_element(By.ID, "submitButton").click()
