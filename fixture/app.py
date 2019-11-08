# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper

class App:
    def __init__(self):
        self.wd = webdriver.Chrome("D:\\Projects\\chromedriver.exe")
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

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


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destr(self):
        self.wd.quit()