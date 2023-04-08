from playwright.sync_api import Page

class DuckDuckSearchPage:

    URL = "https://duckduckgo.com/"

    def __init__(self, page:Page) -> None:
        self.page = page
        self.search_bar= page.get_by_placeholder('Search the web without being tracked')

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_bar.fill(phrase)   