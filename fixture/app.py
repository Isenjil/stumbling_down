# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class App:
    def __init__(self):
        self.wd = webdriver.Chrome("D:\\Projects\\chromedriver.exe")
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destr(self):
        self.wd.quit()
