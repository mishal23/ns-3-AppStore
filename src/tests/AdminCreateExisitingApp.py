# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AdminCreateExisitingApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_admin_create_exisiting_app(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin@appstore.ns3.com")
        driver.find_element_by_id("submit-id-sign_in").click()
        driver.find_element_by_link_text("admin").click()
        driver.find_element_by_link_text("Create a New App").click()
        driver.find_element_by_id("id_title").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("HackVerse")
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("hackverse")
        driver.find_element_by_id("id_app_type").click()
        Select(driver.find_element_by_id("id_app_type")).select_by_visible_text("Fork")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[3]/following::option[2]").click()
        driver.find_element_by_id("id_abstract").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_abstract | ]]
        driver.find_element_by_id("id_abstract").click()
        driver.find_element_by_id("id_abstract").clear()
        driver.find_element_by_id("id_abstract").send_keys("HackVerse is a module in ns-3")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("Amazing module very usseful")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_editors | label=admin <admin@appstore.ns3.com>]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[6]/following::option[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[6]/following::button[1]").click()
        self.assertEqual("django.db.utils.IntegrityError", driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='(most recent call last)'])[1]/preceding::h1[1]").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
