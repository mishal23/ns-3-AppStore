# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDownload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_download(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin@appstore.ns3.com")
        driver.find_element_by_id("submit-id-sign_in").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Models to support applications and scenarios for first responders'])[1]/following::h5[1]").click()
        driver.find_element_by_link_text("Editor Actions").click()
        driver.find_element_by_link_text("Add/Edit Download").click()
        driver.find_element_by_id("id_download_option").click()
        Select(driver.find_element_by_id("id_download_option")).select_by_visible_text("Point to a URL of your Choice")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::option[3]").click()
        driver.find_element_by_id("id_default_release").click()
        Select(driver.find_element_by_id("id_default_release")).select_by_visible_text("Public Safety Communications 0.1")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::option[2]").click()
        driver.find_element_by_id("id_external_url").click()
        driver.find_element_by_id("id_external_url").clear()
        driver.find_element_by_id("id_external_url").send_keys("ht")
        driver.find_element_by_id("id_external_url").send_keys(Keys.DOWN)
        driver.find_element_by_id("id_external_url").clear()
        driver.find_element_by_id("id_external_url").send_keys("https://abcd.tar")
        driver.find_element_by_id("submit-id-maintenance").click()
        self.assertEqual("Download Details modified Successfully!", driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='← Go back to App Page'])[1]/following::h3[1]").text)
    
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
