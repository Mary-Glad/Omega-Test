from playwright.sync_api import Page

class OmegaFormPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.non_uk_company_button = page.locator('div#APPLY_NO_UK_COMPANY')
        self.first_name_input = page.locator('input[placeholder="First Name"]')
        self.last_name_input = page.locator('input[placeholder="Last Name"]')
        self.country__of_residence_input = page.locator('input[placeholder="Country of Residence"]')
        self.company_name_input = page.locator('input[placeholder="Company Name"]')
        self.email_input = page.locator('input[placeholder="Email"]')
        self.website_input = page.locator('input[placeholder="Website"]')
        self.submit_button = page.locator('div#APPLY_SUBMIT')

    def non_uk_company_application(self) -> None:
        self.non_uk_company_button.click()

    def enter_first_name(self, text) -> None:
        self.first_name_input.fill(text)

    def enter_last_name(self, text) -> None:
        self.last_name_input.fill(text)

    def enter_country__of_residence(self, text) -> None:
        self.country__of_residence_input.fill(text)

    def enter_company_name(self, text) -> None:
        self.company_name_input.fill(text)

    def enter_email(self, text) -> None:
        self.email_input.fill(text)
    
    def enter_website(self, text) -> None:
        self.website_input.fill(text)
    
    def submit(self) -> None:
        self.submit_button.click()
