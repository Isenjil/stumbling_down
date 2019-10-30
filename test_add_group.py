# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome("D:\\Projects\\chromedriver.exe")
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.add_new_group(Group(name="Nothing", header="Something from Budha", footer="No environment at all"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.add_new_group(Group(name="", header="", footer=""))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
        self.return_to_groups()

    def submit_form(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def add_new_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_form()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    # def is_element_present(self, how, what):
    #     try:
    #         self.wd.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.wd.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
