from .base_page import BasePage
from .locators import AddProductLocators


class ProductPage(BasePage):
    def should_add_product_to_basket(self):
        assert self.is_element_present(*AddProductLocators.ADD_LINK), "Add to basket is not presented"

    def add_to_basket(self):
        link = self.browser.find_element(*AddProductLocators.ADD_LINK)
        link.click()

    def price_good_to_basket(self):
        price = self.browser.find_element(*AddProductLocators.PRICE_BOOK)
        price_basket = self.browser.find_element(*AddProductLocators.PRICE_BASKET)
        assert price.text == price_basket.text, "Price to basket don't mean price book "

    def name_good_to_basket(self):
        name_book = self.browser.find_element(*AddProductLocators.NAME_BOOK)
        name_book_to_basket = self.browser.find_element(*AddProductLocators.NAME_BOOK_TO_BASKET)
        assert name_book.text == name_book_to_basket.text, "Name to basket don't mean name book"