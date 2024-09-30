import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.description("Test buy product")
def test_buy_product():
     """Тест по покупке товара включает: в себя авторизацию, выбор товара, заполнение данных получателя."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print('Старт теста.')

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product()

    cp = CartPage(driver)
    cp.product_confirmation()

    cip = ClientInfoPage(driver)
    cip.client_info()

    print('Тест завершен.')
    driver.quit()

