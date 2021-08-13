import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add?: '))
        elements_remove = int(input('How many elements will you remove?: '))
        total_element = elements_added - elements_remove


        sleep(3)

        for i in range(elements_added):
            add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
            add_button.click()

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("you're trying to delete more elements the existent")
                break
        
        if total_element > 0:
            print(f"There are {total_element} elements en screen")
        else:
            print("there 0 are elements on screen")

        sleep(3)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)