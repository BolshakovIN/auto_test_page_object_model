from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.name_good_to_basket()
    page.price_good_to_basket()