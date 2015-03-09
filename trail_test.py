__author__ = 'Prashanthi'
# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
import os
import unittest
from helper import Helper
from time import sleep

from selenium import webdriver




class AutomationTest(unittest.TestCase):

    def setUp(self):
        # chrome
        self.driver = webdriver.Chrome("/usr/bin/chromedriver")

        # Go to page needed
        self.driver.get(Helper.URL)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_title(self):
        try:
            title = self.driver.title
            #self.assertEqual(Helper.title,title,"title does not contain ")
            value = self.driver.find_element_by_xpath('//*[@id="slider-carousel"]/div[2]/div[1]/article/a[1]/div[2]/h2')
            value.get_attribute('value')


        except Exception as e:
            print("exception in test_title"+e.message)
            raise Exception(e.message)

    def test_article_1(self):
        try:
            data_article_list = self.driver.find_elements_by_class_name('clickable-article')
            data_article_list[0].click()
            sleep(3)
            new_page_element = self.driver.find_element_by_id('sidebar')
            new_page_element_visible = new_page_element.is_displayed()

            self.assertTrue(new_page_element_visible,"new page element not found")

        except Exception as e:
            print("exception in test_article_1"+e.message)
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()