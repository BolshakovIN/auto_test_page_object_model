from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD_1 = (By.ID, 'id_registration-password1')
    PASSWORD_2 = (By.ID, 'id_registration-password2')
    SUBMIT = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_LINK = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE_BOOK = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    PRICE_BASKET = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    NAME_BOOK = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    NAME_BOOK_TO_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_GOOD = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-block')
    BASKET_CLEAR = (By.CSS_SELECTOR, '#content_inner > p')
