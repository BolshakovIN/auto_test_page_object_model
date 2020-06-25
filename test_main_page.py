from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.text_basket_should_be_present()





# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page = MainPage(browser, link)
#     # открываем страницу
#     page.open()
#              # выполняем метод страницы - переходим на страницу логина
#     page.go_to_login_page()
#     Login_page = LoginPage(browser, browser.current_url)
#     Login_page.should_be_login_page()
#
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
