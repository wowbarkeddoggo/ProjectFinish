import datetime

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver

    # Метод для определения текущего url

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий url: {get_url}')

    # Метод для проверки авторизации, парсим имя пользователя, которое указано в профиле.

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Проверка на слово пройдена.')

    # Метод для скринов

    def screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\ds225\\PycharmProjects\\ProjectFinish\\screens/' + name_screenshot)

    # Метод для проверки url

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Проверка на url пройдена.')

    # Метод для перемещения к объекту взаимодействия

    def move_to_element(self, getter):
        actions = ActionChains(self.driver)
        actions.move_to_element(getter).perform()

    # Методы для сравнения цен товара
    def assert_price_1(self, price1, price2):
        assert price1 == price2
        print("Цена на странице товара и в корзине совпадают.")

    def assert_price_2(self, price1, price2):
        assert price1 == price2
        print("Цена в корзине и на странице оформления заказа совпадают.")

    # Методы для сравнения наименования товара

    def assert_name_1(self, name1, name2):
        assert name1 == name2
        print("Наименование на странице товара и в корзине совпадает.")

    def assert_name_2(self, name1, name2):
        assert name1 == name2
        print("Наименование в корзине и на странице оформления заказа совпадает.")

