# -*- coding: utf-8 -*-


def test_add_contact(appl):
    appl.session.login(username="admin", password="secret")
    appl.contact.add_new_contact()
    appl.session.logout()


def test_delete_contact(appl):
    appl.session.login(username="admin", password="secret")
    appl.contact.delete_first_contact()
    appl.session.logout()
