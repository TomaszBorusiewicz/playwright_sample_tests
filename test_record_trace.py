from playwright.sync_api import sync_playwright


def test_123():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto("https://playwright.dev")
        context.tracing.stop(path="trace.zip")
