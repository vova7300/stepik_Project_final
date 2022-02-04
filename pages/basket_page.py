from base_page import BasePage
from locators import BasketPageLocators


class BasketPage(BasePage):

    def should_product_cart_is_empty(self):
        message = self.browser.find_elements(*BasketPageLocators.BASKET_MESSAGE)[0].text
        print(message)
        assert message == "Your basket is empty. Continue shopping", "Your basket is not empty"

    def should_not_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), "Your basket is empty"
