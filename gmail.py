__author__ = 'Prashanthi'
# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
import os
import unittest
from helper import Gmail_Helper
from time import sleep

from selenium import webdriver




class AutomationTest(unittest.TestCase):

    def setUp(self):
        # chrome
        self.driver = webdriver.Chrome("/usr/bin/chromedriver")

        # Go to page needed
        self.driver.get(Gmail_Helper.URL)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_title(self):
        try:
            title = self.driver.title
            self.assertIn(Gmail_Helper.title,title,"title does not contain ")

        except Exception as e:
            print("exception in test_title"+e.message)
            raise Exception(e.message)

    def login(self):
        try:
            username_box = self.driver.find_element_by_id('Email')
            username_box.send_keys(Gmail_Helper.username)

            self.driver.find_element_by_id('Passwd').send_keys(Gmail_Helper.password)
            self.driver.find_element_by_id('signIn').click()

            sleep(3)
            #self.driver.find_element_by_id()

        except Exception as e:
            print("exception in login"+e.message)
            raise Exception(e)

    def login_no_username(self):
        try:
            username_box = self.driver.find_element_by_id('Email')
            #username_box.send_keys(Gmail_Helper.username)

            self.driver.find_element_by_id('Passwd').send_keys(Gmail_Helper.password)
            self.driver.find_element_by_id('signIn').click()

            sleep(3)
            #self.driver.find_element_by_id()

        except Exception as e:
            print("exception in login"+e.message)
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()