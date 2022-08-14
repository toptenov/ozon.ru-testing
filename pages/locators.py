from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, '//div[@data-widget="webSale"]//button//span[text()="Добавить в корзину"]')