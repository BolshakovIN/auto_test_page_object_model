from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_LINK), "Add to basket is not presented"

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_LINK)
        link.click()

    def price_good_to_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET)
        assert price.text == price_basket.text, "Price to basket don't mean price book "

    def name_good_to_basket(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name_book_to_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_TO_BASKET)
        assert name_book.text == name_book_to_basket.text, "Name to basket don't mean name book"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should not disappear"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear"



