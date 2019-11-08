# -*- coding: utf-8 -*-
from fixture.app import App
import pytest

@pytest.fixture
def appl(request):
    fixture = App()
    request.addfinalizer(fixture.destr)
    return fixture