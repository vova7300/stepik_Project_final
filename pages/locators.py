from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, " #login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, " #login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, " #register_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, " .btn-add-to-basket")

    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

    NAME = (By.CSS_SELECTOR, '.product_main h1')

    ALERT_LIST = (By.CSS_SELECTOR, '.alertinner strong')