from playwright.sync_api import Page
def test_basic_google(page:Page) -> None:
    page.goto("https://duckduckgo.com/")
    page.get_by_placeholder('Search the web without being tracked').fill("TEST")
    page.keyboard.press("Enter")