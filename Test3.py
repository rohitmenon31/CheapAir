import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test3() -> None:
 with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cheapoair.ca/")
    page.get_by_role("tab", name="Packages").click()
    page.get_by_label("To where?").click()
    page.get_by_label("To where?").fill("bom")
    page.get_by_label("To where?").press("Enter")
    page.get_by_label("21 January").click()
    page.get_by_label("13 February").click()
    page.get_by_role("button", name="Search Packages").click()
    page.locator("div").filter(has_text="Here’s the total price for").nth(1).click()
    page.locator("div").filter(has_text="Here’s the total price for").nth(1).click()
    page.get_by_label("Close Modal").click()
    page.get_by_label("Select Package with 5 Star Rating hotel at C$7398.16 Per person Flight+Hotel (").click()

    # ---------------------
    

