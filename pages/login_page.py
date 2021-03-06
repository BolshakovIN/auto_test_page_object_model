from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "'login' not in current url"
        #assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), 'Is not form, for user login'
        #assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_LINK), 'Is not form, for user register'
        #assert True

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password_1_input = self.browser.find_element(*LoginPageLocators.PASSWORD_1)
        password_2_input = self.browser.find_element(*LoginPageLocators.PASSWORD_2)
        email_input.send_keys(email)
        password_1_input.send_keys(password)
        password_2_input.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT)
        submit_button.click()

