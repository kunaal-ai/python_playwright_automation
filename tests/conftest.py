import pytest

from pages.search import DuckDuckSearchPage
from playwright.sync_api import Page

@pytest.fixture
def search_page(page: Page)-> DuckDuckSearchPage:
    return DuckDuckSearchPage(page)