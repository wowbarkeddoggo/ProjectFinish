import time

import allure

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from bs4 import BeautifulSoup
from pages import main_page
from utilities.logger import Logger

value_price_product_in_finish = None
value_name_product_in_finish = None
fake = Faker("en_US")


class ClientInfoPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    delivery_type = '//*[@id="app"]/main/div/section/form/section/main/div[1]/div[2]/label[1]/div'
    param_of_delivery = '//*[@id="app"]/main/div/section/form/section/main/div[2]/div[2]/div[1]/label/div'
    address_of_delivery = '//*[@id="app"]/main/div/section/form/section/main/div[2]/div[3]/div[1]/div[1]/input'
    number_of_flat = '//*[@id="app"]/main/div/section/form/section/main/div[2]/div[3]/div[2]/div[1]/input'
    payment_type = '//*[@id="app"]/main/div/section/form/section/main/div[3]/div[1]/div[2]/label[1]/div'
    value_price_product = '//*[@id="app"]/main/div/section/form/section/aside/div[4]/span[2]'
    value_name_product = ('#app > main > div > section > div.grid.gap-10.grid-cols-1.md\:grid-cols-cart-grid.my-8 > div > div.swiper-wrapper > div > a > img')

    # Getters
    def get_delivery_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_type)))

    def get_param_of_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.param_of_delivery)))

    def get_address_of_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_of_delivery)))

    def get_number_of_flat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_of_flat)))

    def get_payment_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_type)))

    def get_value_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_price_product)))

    def get_value_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.value_name_product)))

    # Actions

    def click_delivery_type(self):
        self.get_delivery_type().click()
        time.sleep(5)
        print("Способ получения: Самовывоз/Курьером")

    def click_param_of_delivery(self):
        self.get_param_of_delivery().click()
        time.sleep(5)
        print("Параметры доставки: Курьерская доставка по Москве")

    def input_address_of_delivery(self, address):
        self.get_address_of_delivery().click()
        self.get_address_of_delivery().send_keys(address)
        time.sleep(10)
        print(f"Параметры доставки: заполнен адрес {address}")

    def input_number_of_flat(self, flat):
        self.get_number_of_flat().click()
        self.get_number_of_flat().send_keys(flat)
        time.sleep(10)
        print(f"Параметры доставки: заполнена квартира {flat}")

    def click_payment_type(self):
        self.move_to_element(self.get_payment_type())
        self.get_payment_type().click()
        print("Способ оплаты: Курьеру наличными")

    def save_price_product_in_finish(self):
        price_product_in_finish = self.get_value_price_product()
        global value_price_product_in_finish
        value_price_product_in_finish = price_product_in_finish.text
        print(f'Цена на странице оформления заказа: {value_price_product_in_finish}')
        return value_price_product_in_finish

    def save_name_product_in_finish(self):
        img_element = self.get_value_name_product()
        img_html = img_element.get_attribute('outerHTML')
        soup = BeautifulSoup(img_html, 'html.parser')
        img_tag = soup.find('img')
        global value_name_product_in_finish
        value_name_product_in_finish = img_tag.get('alt')
        print(f'Наименование на странице оформления заказа: {value_name_product_in_finish}')
        return value_name_product_in_finish


    # Methods

    def client_info(self):
        with allure.step("Client info"):
            Logger.add_start_step(method="client_info")
            self.get_current_url()
            self.click_delivery_type()
            self.click_param_of_delivery()
            self.input_address_of_delivery('Б. Грузинская ул., 1, Москва, 123242')
            self.input_number_of_flat('1')
            self.click_payment_type()
            self.save_price_product_in_finish()
            self.save_name_product_in_finish()
            self.screenshot()
            self.assert_price_2(main_page.value_price_catalog_text, value_price_product_in_finish)
            self.assert_name_2(main_page.value_name_catalog_text, value_name_product_in_finish)
            Logger.add_end_step(url=self.driver.current_url, method="client_info")

