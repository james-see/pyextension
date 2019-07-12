"""Test pyfileinfo."""
from bs4 import BeautifulSoup

import pytest

import requests


@pytest.fixture()
def extension():
    """Test extension to use."""
    return "doc"


def test_getfileinfo_for_extension(extension):
    """Ensure we are getting text from the fileinfo site."""
    r = requests.get(f"https://fileinfo.com/extension/{extension}")
    soup = BeautifulSoup(r.text, 'lxml')
    ahrefs = soup.findAll("span", {"itemprop": "description"})
    for item in ahrefs:
        assert item.text != ""
