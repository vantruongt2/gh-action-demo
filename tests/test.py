import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class TestPage(unittest.TestCase):
    def setUp(self):
        self.url = os.getenv('URL')
        print(self.url)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            options=webdriver.ChromeOptions()
        )

    def test_content(self):
        self.driver.get(self.url)
        ele = self.driver.find_element(By.ID, "wf")
        self.assertEqual(ele.text, 'Workflows')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
