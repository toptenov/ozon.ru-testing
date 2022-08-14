from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def is_add_tocart_button_on_product_page(self):
        assert self.is_element_presented(*ProductPageLocators.ADD_TO_CART_BUTTON),\
            f"Add to cart button is not on the Product Page"