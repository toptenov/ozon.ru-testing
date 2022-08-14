import pytest

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


@pytest.mark.parametrize(
    "product_url",
    [("https://www.ozon.ru/product/smartfon-xiaomi-redmi-9a-2-32-gb-seryy-311308821/")]
)
class TestProductPage():
    def test_add_to_cart_button_is_on_product_page(self, browser, product_url):
        page = ProductPage(browser, product_url)
        page.open()
        page.is_add_tocart_button_on_product_page()
    
    def test_product_is_in_cart_after_pressing_add_to_cart_button(self, browser, product_url):
        page = ProductPage(browser, product_url)
        page.open()
        page.is_cart_empty()
        page.click_add_product_to_cart_button()
        page.is_one_product_in_cart()
