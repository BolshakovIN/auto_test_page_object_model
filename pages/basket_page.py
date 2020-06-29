from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOOD), \
            "There should be no items in the list"

    def text_basket_should_be_present(self):
        basket_clear_alert = 'basket is empty'
        basket_clear = self.browser.find_element(*BasketPageLocators.BASKET_CLEAR).text
        assert basket_clear_alert in basket_clear, 'To basket have not text "basket empty"'
