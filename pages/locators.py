from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    ADD_BOOK_TO_CART_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    BOOK_NAME_IN_ALERT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong')
    PRICE_IN_ALERT = (By.XPATH, '/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong')
    PRICE_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div')
    BOOK_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.XPATH, '//div[2]/span/a')


class CartPageLocators():
    PRODUCT_ADD_TO_CART_SECTION = (By.XPATH, '//*[@id="basket_formset"]/div')
    CART_IS_EMPTY_TEXT= (By.XPATH, '//*[@id="content_inner"]/p')

