# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AdminEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_admin_edit(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin@appstore.ns3.com")
        driver.find_element_by_id("submit-id-sign_in").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Models to support applications and scenarios for first responders'])[1]/following::h5[1]").click()
        driver.find_element_by_link_text("Editor Actions").click()
        driver.find_element_by_link_text("Edit Details").click()
        driver.find_element_by_id("id_description").click()
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("This module provides extensions to the LTE including Device to Device (D2D) capabilities, as well as new propagation models and applications related to public safety communications.\n\nThe current model is based on ns-3.29 release and supports the following additional features.")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::button[1]").click()
        self.assertEqual("Edited Details Successfully!", driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='← Go back to App Page'])[1]/following::h3[1]").text)
    
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
