from playwright.sync_api import Page

class OmegaMainPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.get_started_button = page.locator('a#TOOLBAR_GET_STARTED')
    
    def navigate(self) -> None:
        self.page.goto('https://omg.one')
    
    def complete_the_application(self) -> None:
        self.get_started_button.click()
