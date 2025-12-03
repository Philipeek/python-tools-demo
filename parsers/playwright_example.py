from playwright.sync_api import sync_playwright

def run_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Demo website (public and legal to scrape)
        page.goto("https://example.com")

        title = page.title()
        print("Page title:", title)

        browser.close()

if __name__ == "__main__":
    run_demo()
