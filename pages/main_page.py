from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

# class MainPage(BasePage):
#     def go_to_login_page(self):
#         #assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented!!!:("
#         link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         link.click()
#         #return LoginPage(browser=self.browser, url=self.browser.current_url)
#
#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented!!!:("
