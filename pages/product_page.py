from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def is_add_tocart_button_on_product_page(self):
        assert self.is_element_presented(*ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON),\
            f"Add to cart button is not on the Product Page"
    
    def is_cart_empty(self):
        header_cart_icon = self.get_element(*ProductPageLocators.HEADER_EMPTY_CART_ICON)
        assert header_cart_icon.text == "0", "The cart is not empty"

    def is_one_product_in_cart(self):
        header_cart_icon = self.get_element(*ProductPageLocators.HEADER_NOT_EMPTY_CART_ICON)
        assert header_cart_icon.text == "1", f"{header_cart_icon.text} products in the cart instead of 0"

    def click_add_product_to_cart_button(self):
        self.click_on_element(*ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON)
