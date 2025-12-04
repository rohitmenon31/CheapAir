import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test2() -> None:
    try:
        with sync_playwright() as playwright:
            # Launch Chromium in headless mode
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            
            # Navigate to CheapOair
            page.goto("https://www.cheapoair.ca/")
            
            # Perform the test actions
            page.get_by_role("tab", name="Packages").click()
            page.get_by_label("To where?").fill("lond")
            page.get_by_text("LON - London All Airports,").click()
            
            # Choose dates
            page.get_by_label("27 December 2024").click()
            page.get_by_label("29 January").click()
            
            # Search packages
            page.get_by_role("button", name="Search Packages").click()
            
            # Optional: wait for results to appear
            page.wait_for_selector("text=Package Results")  # adjust selector if needed
            
            print("Test2 completed successfully!")

    except Exception as e:
        print(f"Test2 failed: {e}")
        raise  # ensures Jenkins marks build as failed

    finally:
        context.close()
        browser.close()

if __name__ == "__main__":
    test2()






