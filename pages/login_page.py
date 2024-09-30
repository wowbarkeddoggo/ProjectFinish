import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    url = 'https://moychay.ru'

    # Locators
    user_button_container = '//*[@id="app"]/main/header/div/div/div[1]/nav/div[1]/div/a'
    user_login = '//*[@id="form"]/input[1]'
    password = '//*[@id="form"]/input[2]'
    button_login = '//*[@id="form"]/button'
    main_word = '//*[@id="app"]/main/header/div/div/div[1]/nav/div[1]/div/div[1]/span[1]'

    # Getters

    def get_user_button_container(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_button_container)))

    def get_user_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_user_button_container(self):
        self.get_user_button_container().click()
        print("Клик по кнопке Войти на главной странице для перехода к форме авторизации.")

    def input_user_login(self, user_name):
        self.get_user_login().send_keys(user_name)
        print(f"Логин введен: {user_name}.")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print(f"Пароль введен: {password}.")

    def click_button_login(self):
        time.sleep(5)
        self.get_button_login().click()
        print("Клик по кнопке Войти.")

    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_user_button_container()
            self.input_user_login('Вставьте сюда свой логин')
            self.input_password('Вставьте сюда свой пароль')
            self.click_button_login()
            self.assert_word(self.get_main_word(), 'Вставьте сюда имя или фио, которое указано в профиле')
            self.screenshot()
            self.assert_url('https://moychay.ru/auth')
            Logger.add_end_step(url=self.driver.current_url, method="authorization")



