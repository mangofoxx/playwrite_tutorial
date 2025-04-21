from playwright.sync_api import expect, Page

def test_basic_duck_serach(page: Page) -> None:
    # Given the DuckCuckGo home page is displayed
    page.goto('https://duckduckgo.com/')
    # When the user searches for the phrase
    page.locator('id=searchbox_input').fill('panda')
    page.locator("button[aria-label='Search']").click()
    # Then the search is the phrase
    expect(page.locator('id=search_form_input')).to_have_value('panda')
    # And the search result links pertain to the phrase
    # And tge search result title contains the phrase
    pass