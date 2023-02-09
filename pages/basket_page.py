from pages.base_page import BasePage
from pages.locators import CartPageLocators


class BasketPage (BasePage):
    def check_cart_is_empty_text_present(self):
        assert self.is_element_present(*CartPageLocators.CART_IS_EMPTY_TEXT), "TEXT 'Cart is not empty' NOT present "

    def check_cart_is_empty(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_ADD_TO_CART_SECTION), "Cart is not empty"


