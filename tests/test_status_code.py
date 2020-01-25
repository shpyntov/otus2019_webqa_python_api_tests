import requests
import pytest


@pytest.fixture
def request_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def exp_status_code(request):
    return request.config.getoption('--status_code')


def test_status_code_by_url(request_url, exp_status_code):
    assert requests.get(request_url).status_code == int(exp_status_code)
