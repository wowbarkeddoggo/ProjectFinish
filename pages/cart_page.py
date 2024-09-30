import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages import main_page
from utilities.logger import Logger

value_price_product_in_cart = None
value_name_product_in_cart = None


class CartPage(Base):

    # Locators
    checkout_button = '//*[@id="app"]/main/section/div/div/section/aside/div[2]/button[2]'
    value_price_product = '//*[@id="app"]/main/section/div/div/section/aside/div[1]/div[2]/div[2]'
    value_name_product = '//*[@id="app"]/main/section/div/div/section/main/div/div[2]/div/div[2]/div[1]/a'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_value_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_price_product)))

    def get_value_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_name_product)))

    # Actions

    def click_checkout_button(self):
        time.sleep(10)
        self.get_checkout_button().click()
        time.sleep(10)
        print("Переход на страницу оформления.")

    def save_price_product_in_cart(self):
        price_product_in_cart = self.get_value_price_product()
        global value_price_product_in_cart
        value_price_product_in_cart = price_product_in_cart.text
        print(f'Цена на странице корзины: {value_price_product_in_cart}')
        return value_price_product_in_cart

    def save_name_product_in_cart(self):
        name_product_in_cart = self.get_value_name_product()
        global value_name_product_in_cart
        value_name_product_in_cart = name_product_in_cart.text
        print(f'Наименование на странице корзины: {value_name_product_in_cart}')
        return value_name_product_in_cart

    # Methods

    def product_confirmation(self):
        with allure.step("Product confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.get_current_url()
            self.save_price_product_in_cart()
            self.save_name_product_in_cart()
            self.click_checkout_button()
            self.screenshot()
            self.assert_url('https://moychay.ru/checkout')
            self.assert_price_1(main_page.value_price_catalog_text, value_price_product_in_cart)
            self.assert_name_1(main_page.value_name_catalog_text, value_name_product_in_cart)
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")
