# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_main(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("Something")
        wd.find_element_by_name("middlename").send_keys("diabolical")
        wd.find_element_by_name("lastname").send_keys("BH Gang")
        wd.find_element_by_name("nickname").send_keys("test")
        wd.find_element_by_name("title").send_keys("TEST")
        wd.find_element_by_name("company").send_keys("Test Company LTD")
        wd.find_element_by_name("address").send_keys("Ocean Drive")
        wd.find_element_by_name("home").send_keys("555-72-81")
        wd.find_element_by_name("mobile").send_keys("+1-778-319-02-18")
        wd.find_element_by_name("work").send_keys("555-81-72")
        wd.find_element_by_name("email").send_keys("test@test.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("21")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("May")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1985")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("21")
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("May")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2085")
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("Nothing")
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("Pennywise ave, 142")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys("Test account")
        wd.find_element_by_xpath("//input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # self.return_to_main()
        # wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
