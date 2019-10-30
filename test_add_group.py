# -*- coding: utf-8 -*-
from app import App
from group import Group
import pytest


@pytest.fixture
def appl(request):
    fixture = App()
    request.addfinalizer(fixture.destr)
    return fixture


def test_add_group(appl):
    appl.login(username="admin", password="secret")
    appl.add_new_group(Group(name="Nothing", header="Something from Budha", footer="No environment at all"))
    appl.logout()


def test_add_empty_group(appl):
    appl.login(username="admin", password="secret")
    appl.add_new_group(Group(name="", header="", footer=""))
    appl.logout()
