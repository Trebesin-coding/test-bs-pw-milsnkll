from playwright.sync_api import sync_playwright


login = "Jarmil"
password = "Admin123"

def main():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://souhrada.github.io/playwright-exam/")
        page.fill('input#login', login)
        page.fill('input#pass', password)
        page.click('button.login-btn')
        text = page.locator('p.super-secret-text').text_content()
        print(text)

        input("blabla")
        browser.close()
    

if __name__ == "__main__":
    main()