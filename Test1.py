import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test1() -> None:
    try:
        with sync_playwright() as playwright:
            # Launch Chromium in headless mode (works in Jenkins)
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            
            # Open CheapOair
            page.goto("https://www.cheapoair.ca/")
            
            # Fill "To where?"
            page.get_by_label("To where?").click()
            page.get_by_label("To where?").fill("bom")
            page.get_by_text("BOM - Mumbai, India").click()
            
            # Choose dates
            page.get_by_label("Choose a departure date.").click()
            page.get_by_label("20 December 2024").click()
            page.get_by_label("28 December 2024").click()
            
            # Search flights
            page.get_by_role("button", name="Search Flights").click()
            
            # Optional: wait for results to load
            page.wait_for_selector("text=Flight Results")  # adjust selector if needed
            
            print("Test1 completed successfully!")

    except Exception as e:
        print(f"Test1 failed: {e}")
        raise  # This ensures Jenkins marks the build as failed

    finally:
        context.close()
        browser.close()

if __name__ == "__main__":
    test1()



