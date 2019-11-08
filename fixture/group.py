# -*- coding: utf-8 -*-


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def submit_form(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def add(self, group):
        wd = self.app.wd
        self.return_to_groups()
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

    def delete_first(self):
        wd = self.app.wd
        self.return_to_groups()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete first group
        wd.find_element_by_name("delete").click()


