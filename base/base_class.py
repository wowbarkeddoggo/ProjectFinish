import datetime

from selenium.webdriver import ActionChains


class Base():
    """ Базовый класс, содержащий универсальные методы """
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """ Метод для определения текущего url """
        get_url = self.driver.current_url
        print(f'Текущий url: {get_url}')

    def assert_word(self, word, result):
        """ Метод для проверки авторизации, парсим имя пользователя, которое указано в профиле. """
        value_word = word.text
        assert value_word == result
        print('Проверка на слово пройдена.')

    def screenshot(self):
     """ Метод для создания скриншотов. """
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\ds225\\PycharmProjects\\ProjectFinish\\screens/' + name_screenshot)


    def assert_url(self, result):
        """ Метод для проверки url. """
        get_url = self.driver.current_url
        assert get_url == result
        print('Проверка на url пройдена.')


    def move_to_element(self, getter):
        """ Метод для перемещения к объекту взаимодействия. """
        actions = ActionChains(self.driver)
        actions.move_to_element(getter).perform()

    def assert_price_1(self, price1, price2):
        """ Метод для сравнения цен товара. """
        assert price1 == price2
        print("Цена на странице товара и в корзине совпадают.")

    def assert_price_2(self, price1, price2):
        """ Метод для сравнения цен товара. """
        assert price1 == price2
        print("Цена в корзине и на странице оформления заказа совпадают.")


    def assert_name_1(self, name1, name2):
        """ Метод для сравнения наименования товара. """
        assert name1 == name2
        print("Наименование на странице товара и в корзине совпадает.")

    def assert_name_2(self, name1, name2):
        """ Метод для сравнения наименования товара. """
        assert name1 == name2
        print("Наименование в корзине и на странице оформления заказа совпадает.")

