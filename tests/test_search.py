from playwright.sync_api import Page
from pages.search import DuckDuckSearchPage

def test_basic_google(page:Page) -> None:
    search_page = DuckDuckSearchPage(page)
    search_page.load()
    search_page.search('Panda')
    page.keyboard.press('Enter')