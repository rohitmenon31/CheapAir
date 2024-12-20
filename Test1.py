import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test1() -> None:
 with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cheapoair.ca/")
    page.get_by_label("To where?").click()
    page.get_by_label("To where?").fill("bom")
    page.get_by_text("BOM - Mumbai, India").click()
    page.get_by_label("Choose a departure date.").click()
    page.get_by_label("20 December 2024").click()
    page.get_by_label("28 December 2024").click()
    page.get_by_role("button", name="Search Flights").click()

    context.close()
    browser.close()

