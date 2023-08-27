import pytest
from playwright.sync_api import expect, Page

from pages.omega_main import OmegaMainPage
from pages.omega_form import OmegaFormPage

def test_non_uk_application(page: Page) -> None:
    
    omega_main_page = OmegaMainPage(page)
    omega_form_page = OmegaFormPage(page)

    # The openning of the Omega home page
    omega_main_page.navigate()

    # Filling out a form (Get started today)
    omega_main_page.complete_the_application()

    omega_form_page.non_uk_company_application()

    omega_form_page.enter_first_name('Mary')
       
    omega_form_page.enter_last_name('Gladkova')
       
    omega_form_page.enter_country__of_residence('France')
    
    omega_form_page.enter_company_name('Omega is a brilliant company')

    omega_form_page.enter_email('glad.mary.ol0@gmail.com')
    
    omega_form_page.enter_website('omg.one')
    
    #omega_form_page.submit()
