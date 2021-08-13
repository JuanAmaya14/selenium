from time import sleep
import unittest
from selenium import webdriver

class SearchGoolge(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com/')

    def test_search(self):
        driver = self.driver

        search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.send_keys('porno')
       
        search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        self.assertTrue(search_button.is_enabled())
        search_button.click()
        sleep(10)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)