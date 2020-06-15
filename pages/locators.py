from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_LINK = (By.CSS_SELECTOR, "#id_registration-email")

class AddProductLocators():
    ADD_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_BOOK = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    PRICE_BASKET = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    NAME_BOOK = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    NAME_BOOK_TO_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
