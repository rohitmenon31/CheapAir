import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test2() -> None:
    with sync_playwright() as playwright: 
        browser = playwright.chromium.launch(headless=True) 
        context = browser.new_context() 
        page = context.new_page()
        
        # Navigate to the website
        page.goto("https://www.cheapoair.ca/")
        
        # Perform the test actions
        page.get_by_role("tab", name="Packages").click()
        page.get_by_label("To where?").fill("lond")
        page.get_by_text("LON - London All Airports,").click()
        page.get_by_label("27 December 2024").click()
        page.get_by_label("29 January").click()
        page.get_by_role("button", name="Search Packages").click()


        # Close the browser
        context.close() 
        browser.close()




