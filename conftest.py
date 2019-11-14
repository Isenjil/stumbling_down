# -*- coding: utf-8 -*-
from fixture.app import App
import pytest

@pytest.fixture(scope = "session")
def appl(request):
    fixture = App()
    request.addfinalizer(fixture.destr)
    return fixture