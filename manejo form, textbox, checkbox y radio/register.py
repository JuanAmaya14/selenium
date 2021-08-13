import unittest
from selenium import webdriver

class AssertionsTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="header-account"]/div/ul/li[6]/a').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_enabled())
        create_account_button.click()

        #self.assertEqual('create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subcription = driver.find_element_by_id('is_subscribed')
        submit_buttom = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled and last_name.is_enabled and email_address.is_enabled
        and password.is_enabled and confirm_password.is_enabled and news_letter_subcription.is_enabled and 
        submit_buttom.is_enabled)

        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@gmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        news_letter_subcription.send_keys('Test')
        submit_buttom.click()


    def tearDown(self):
        self.driver.quit()





if __name__ == "__main__":
    unittest.main(verbosity=2)