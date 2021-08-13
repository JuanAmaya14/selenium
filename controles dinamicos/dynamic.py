import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Nombre_class(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/dynamic_controls')

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        checkbox.click()

        remove_add_botton = driver.find_elements_by_css_selector('#checkbox-example > button')
        remove_add_botton.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkbox-example > button")))
        remove_add_botton.click()

        enable_desable_button = driver.find_element_by_css_selector('#input-example > button')
        enable_desable_button.click()

        WebDriverWait(driver, 15).until((EC.element_to_be_clickable(By.CSS_SELECTOR,'#input-example > button' )))

        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_desable_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)