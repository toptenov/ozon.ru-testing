from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_PRODUCT_TO_CART_BUTTON = (By.XPATH, '//div[@data-widget="webSale"]//button//span[text()="Добавить в корзину"]')
    HEADER_EMPTY_CART_ICON = (By.XPATH, '//a[@href="/cart"]/span[@class="tsCaptionBold c1w cw2"]')
    HEADER_NOT_EMPTY_CART_ICON = (By.XPATH, '//a[@href="/cart"]/span[@class="tsCaptionBold c1w"]')