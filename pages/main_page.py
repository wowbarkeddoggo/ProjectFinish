import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger

value_price_catalog_text = None
value_name_catalog_text = None


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    category_puer = '//*[@id="app"]/main/div/section/section/div/div[1]/aside/ul/li[7]/div'
    cookie_agree_button = '//*[@id="app"]/main/div[2]/div/div/div/div[2]/button'
    shen_puer_pressed = '//*[@id="app"]/main/div/section/section/div/div[1]/aside/ul/li[7]/section/div/ul/li[3]'
    filter_by_newness = '(//div[@class="relative "])[3]'
    filter_from_price_increase = '(//a[@class="text-black hover:text-mc-green-hover"])[1]'
    filter_with_quantity = ('(//button[@class="flex items-center border border-mc-green-100 w-full px-2 sm:px-3 py-1 '
                            'sm:py-2 rounded bg-white dark:bg-gray-900"])[2]')
    filter_with_quantity_24 = ('//*[@id="app"]/main/div/section/section/div/div[2]/section[2]/div[1]/div/div[1]'
                               '/div/div[2]/nav/a[2]/div')
    filter_weight = '//*[@id="product-47123-weight"]/button'
    filter_weight_1 = '//*[@id="product-47123-weight"]/div/button[1]'
    value_price_catalog = ('//*[@id="app"]/main/div/section/section/div/div[2]/section[2]/div[1]/main/section[1]/div[2]/section/div[1]/div[1]')
    value_name_catalog = '//*[@id="app"]/main/div/section/section/div/div[2]/section[2]/div[1]/main/section[1]/a/div[2]'
    add_to_cart_product = '(//div[@class="w-36 sm:w-28 ml-1"])[1]'
    go_to_cart = '//*[@id="app"]/main/header/div/div/div[1]/nav/a[3]'

    # Getters
    def get_category_puer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_puer)))

    def get_cookie_agree_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookie_agree_button)))

    def get_shen_puer_pressed(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.shen_puer_pressed)))

    def get_filter_by_newness(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_by_newness)))

    def get_filter_from_price_increase(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.filter_from_price_increase)))

    def get_filter_with_quantity(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_with_quantity)))

    def get_filter_with_quantity_24(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_with_quantity_24)))

    def get_filter_weight(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_weight)))

    def get_filter_weight_1(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_weight_1)))

    def get_value_price_catalog(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.value_price_catalog)))

    def get_value_name_catalog(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.value_name_catalog)))

    def get_add_to_cart_product(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    # Actions
    def click_category_puer(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.get_category_puer().click()
        print("Выпадающий список в боковом меню: Пуэр")

    def click_cookie_agree_button(self):
        self.driver.execute_script("window.scrollTo(0, 100);")
        self.get_cookie_agree_button().click()
        print("Принимаем куки")

    def click_shen_puer_pressed(self):
        self.get_shen_puer_pressed().click()
        print("Выпадающий список Пуэр -> Шэн пуэр прессованный.")

    def click_filter_by_newness(self):
        self.get_filter_by_newness().click()
        time.sleep(5)
        self.get_filter_by_newness().click()
        print("Сортировка над товарами")

    def click_filter_from_price_increase(self):
        self.get_filter_from_price_increase().click()
        time.sleep(5)
        print("Сортировка по возрастанию цены")

    def click_filter_with_quantity(self):
        time.sleep(3)
        self.get_filter_with_quantity().click()
        print("Сортировка по кол-ву")

    def click_filter_with_quantity_24(self):
        time.sleep(3)
        self.get_filter_with_quantity_24().click()
        time.sleep(5)
        print("Сортировка по кол-ву: 24")

    def click_filter_weight(self):
        self.get_filter_weight().click()
        print("Меню выбора веса чая")

    def click_filter_weight_1(self):
        self.get_filter_weight_1().click()
        time.sleep(10)
        print("Меню выбора веса чая: 1")

    def click_add_to_cart_product(self):
        self.get_add_to_cart_product().click()
        time.sleep(5)
        print("Товар добавлен в корзину.")

    def save_price_product_in_catalog(self):
        price_product_in_catalog = self.get_value_price_catalog()
        global value_price_catalog_text
        value_price_catalog_text = price_product_in_catalog.text
        print(f'Цена на странице выбора товара: {value_price_catalog_text}')
        return value_price_catalog_text

    def save_name_product_in_catalog(self):
        name_product_in_catalog = self.get_value_name_catalog()
        global value_name_catalog_text
        value_name_catalog_text = name_product_in_catalog.text
        print(f'Наименование на странице выбора товара: {value_name_catalog_text}')
        return value_name_catalog_text

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Переход в корзину.")

    # Methods

    def select_product(self):
        with allure.step("Select product"):
            Logger.add_start_step(method="select_product")
            self.get_current_url()
            self.click_category_puer()
            self.click_cookie_agree_button()
            self.click_shen_puer_pressed()
            self.click_filter_by_newness()
            time.sleep(5)
            self.click_filter_from_price_increase()
            self.click_filter_with_quantity()
            self.click_filter_with_quantity_24()
            self.click_filter_weight()
            self.click_filter_weight_1()
            self.save_price_product_in_catalog()
            self.save_name_product_in_catalog()
            self.click_add_to_cart_product()
            self.click_go_to_cart()
            self.screenshot()
            self.assert_url('https://moychay.ru/catalog/puer/shen_puer_pressovannyj?sort=price_up&per=24')
            Logger.add_end_step(url=self.driver.current_url, method="select_product")










