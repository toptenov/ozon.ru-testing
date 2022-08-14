from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_PRODUCT_TO_CART_BUTTON = (By.XPATH, '//div[@data-widget="webSale"]//button//span[text()="Добавить в корзину"]')
    ADD_PRODUCT_TO_FAVORITES_BUTTON = (By.XPATH, '//button[@aria-label="Добавить в избранное"]//span[text()="В избранное"]')
    HEADER_EMPTY_CART_ICON = (By.XPATH, '//a[@href="/cart"]/span[@class="tsCaptionBold c1w cw2"]')
    HEADER_NOT_EMPTY_CART_ICON = (By.XPATH, '//a[@href="/cart"]/span[@class="tsCaptionBold c1w"]')
    HEADER_EMPTY_FAVORITES_ICON = (By.XPATH, '//a[@href="/my/favorites"]/span[@class="tsCaptionBold c1w cw2"]')
    HEADER_NOT_EMPTY_FAVORITES_ICON = (By.XPATH, '//a[@href="/my/favorites"]/span[@class="tsCaptionBold c1w"]')
    ADD_TO_CART_FORM_QUANTITY_OF_PRODUCTS_COUNTER = (By.XPATH, '//div[@data-widget="webAddToCart"]//span[@class="wk4"]')
    