from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_new_year_url(self):
        get_url = self.browser.current_url
        assert "?promo=newYear" in get_url, "'?promo=newYear' is absent in current url"

    def check_assert_book_name_and_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BOOK_TO_CART_MESSAGE)
        message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        print(message)
        print(book_name)
        assert book_name == message, "INCORRECT!"

    def check_assert_price_and_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE)
        message = self.browser.find_element(*ProductPageLocators.PRICE_IN_ALERT).text
        book_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        print(message)
        print(book_price)
        assert book_price == message, "INCORRECT!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.ADD_BOOK_TO_CART_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_BOOK_TO_CART_MESSAGE), "Success message is presented, it is OK"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_BOOK_TO_CART_MESSAGE), "Success message is disappeared"

