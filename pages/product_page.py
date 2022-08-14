from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def is_add_tocart_button_on_product_page(self):
        assert self.is_element_presented(*ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON),\
            f"Add to cart button is not on the Product Page"
    
    def is_cart_empty(self):
        header_cart_icon = self.get_element(*ProductPageLocators.HEADER_EMPTY_CART_ICON)
        assert header_cart_icon.text == "0", "The cart is not empty"

    def is_one_product_in_header_cart_icon(self):
        header_cart_icon = self.get_element(*ProductPageLocators.HEADER_NOT_EMPTY_CART_ICON)
        assert header_cart_icon.text == "1", f"{header_cart_icon.text} products in the cart instead of 1"

    def click_add_product_to_cart_button(self):
        self.click_on_element(*ProductPageLocators.ADD_PRODUCT_TO_CART_BUTTON)

    def is_one_product_in_add_to_cart_form_quantity_of_products_counter(self):
        add_to_cart_form_quantity_of_products_counter = self.get_element(
            *ProductPageLocators.ADD_TO_CART_FORM_QUANTITY_OF_PRODUCTS_COUNTER
        )
        assert add_to_cart_form_quantity_of_products_counter.text == "1",\
            f"Quantity of products {add_to_cart_form_quantity_of_products_counter.text} instead of 1"

    def is_favorites_empty(self):
        header_favorites_icon = self.get_element(*ProductPageLocators.HEADER_EMPTY_FAVORITES_ICON)
        assert header_favorites_icon.text == "0", "The favorites is not empty"

    def click_add_product_to_favorites_button(self):
        self.click_on_element(*ProductPageLocators.ADD_PRODUCT_TO_FAVORITES_BUTTON)

    def is_one_product_in_header_favorites_icon(self):
        header_favorites_icon = self.get_element(*ProductPageLocators.HEADER_NOT_EMPTY_FAVORITES_ICON)
        assert header_favorites_icon.text == "1",\
            f"{header_favorites_icon.text} products in the favorites instead of 1"
