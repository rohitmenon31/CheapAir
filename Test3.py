import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test3() -> None:
    try:
        with sync_playwright() as playwright:
            # Launch Chromium in headless mode
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            # Navigate to CheapOair
            page.goto("https://www.cheapoair.ca/")

            # Click on Packages tab
            page.get_by_role("tab", name="Packages").click()

            # Fill 'To where?' field
            page.get_by_label("To where?").click()
            page.get_by_label("To where?").fill("bom")
            page.get_by_label("To where?").press("Enter")

            # Select travel dates
            page.get_by_label("21 January").click()
            page.get_by_label("13 February").click()

            # Search packages
            page.get_by_role("button", name="Search Packages").click()

            # Interact with results
            page.locator("div").filter(has_text="Here’s the total price for").nth(1).click()
            page.locator("div").filter(has_text="Here’s the total price for").nth(1).click()
            page.get_by_label("Close Modal").click()
            page.get_by_label(
                "Select Package with 5 Star Rating hotel at C$7398.16 Per person Flight+Hotel ("
            ).click()

            # Optional: wait for confirmation
            page.wait_for_selector("text=Booking Summary")  # adjust selector if needed

            print("Test3 completed successfully!")

    except Exception as e:
        print(f"Test3 failed: {e}")
        raise  # ensures Jenkins marks build as failed

    finally:
        context.close()
        browser.close()

if __name__ == "__main__":
    test3()

    



