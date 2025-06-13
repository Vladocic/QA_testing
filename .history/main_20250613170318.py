from playwright.sync_api import sync_playwright, Playwright

chromium = Playwright.chromium
browser = chromium.launch()