# -*- coding: utf-8 -*-
from model.group import Group


def test_add_empty_group(appl):
    appl.session.login(username="admin", password="secret")
    appl.group.add(Group(name="", header="", footer=""))
    appl.session.logout()


def test_add_group(appl):
    appl.session.login(username="admin", password="secret")
    appl.group.add(Group(name="Nothing", header="Something from Budha", footer="No environment at all"))
    appl.session.logout()
