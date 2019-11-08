# -*- coding: utf-8 -*-


def test_delete(appl):
    appl.session.login(username="admin", password="secret")
    appl.group.delete_first()
    appl.session.logout()
