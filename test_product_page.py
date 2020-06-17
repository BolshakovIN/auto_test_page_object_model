from .pages.product_page import ProductPage
import pytest


#@pytest.mark.parametrize('promo_code', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6,
                                        pytest.param(7, marks=pytest.mark.xfail),
                                        8, 9])
def test_guest_can_add_product_to_basket(browser, promo_code):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.name_good_to_basket()
    page.price_good_to_basket()
