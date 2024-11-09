import allure
from selenium.webdriver.remote.webdriver import WebDriver


@allure.epic('Авиабилеты ')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('UI-тесты на авторизацию')
class UITest:

    @allure.id('авторизация ')
    @allure.story('Позитивные проверки авторизации')
    @allure.title('Авторизация ранее зарегистрированного пользователя')
    @allure.description('Выполнить авторизацию ранее зарегистрированного пользователя')
    @allure.feature('AUTHORIZE')
    def auth_test(self, browser: WebDriver, test_data: DataProvider):
        index_page = IndexPage(browser)
        index_page.open()
        index_page.click_sign_in()

        team_page = TeamPage(browser)
        team_page.set_email(test_data.get('email'))
        team_page.set_password(test_data.get('password'))
        team_page.login()

        with allure.step('Проверка: поле Email'):
            with allure.step('Email пользователя отображается в поле'):
                assert test_data.get('email') == 'grishina.natly@gmail.com'

    @allure.id('авторизация ')
    @allure.story('Позитивные проверки авторизации')
    @allure.title('Авторизация ранее зарегистрированного пользователя')
    @allure.description('Выполнить авторизацию ранее зарегистрированного пользователя')
    @allure.feature('AUTHORIZE')
    def auth_test(self, browser: WebDriver, test_data: DataProvider):
        index_page = IndexPage(browser)
        index_page.open()
        index_page.click_sign_in()

        team_page = TeamPage(browser)
        team_page.set_email(test_data.get('email'))
        team_page.set_password(test_data.get('password'))
        team_page.login()

        with allure.step('Проверка: поле password'):
            with allure.step('password пользователя отображается в поле'):
                assert test_data.get('password') == 'UEU9gd_98'

    @allure.id('Проверить поля ”Откуда” и “Куда”, ”Туда ” , “ Обратно ” и  “Туристы”')
    @allure.story('Позитивные проверки авторизации')
    @allure.title('Пользователь авторизован и заказывает билет')
    @allure.description('Выполнить авторизацию ранее зарегистрированного пользователя')
    @allure.feature('AUTHORIZE')
    def auth_test(self, browser: WebDriver, test_data: DataProvider):
        index_page = WebDriver(browser)
        index_page.open()
        index_page.click_sign_in()

        team_page = TeamPage(browser)
        team_page.set_tickets(test_data.get('”Откуда” и “Куда”, ”Туда ” , “ Обратно ” и  “Туристы”'))
        team_page.login()

        with allure.step('”Откуда” и “Куда”, ”Туда ” , “ Обратно ” и  “Туристы”'):
            with allure.step('Пользователь авторизовался и выбирает билет '):
                assert test_data.get('откуда') == 'Москва'
                assert test_data.get('куда') == 'Южная Корея'
                assert test_data.get('туда') == '08.11.2024'
                assert test_data.get('обратно') == '29.11.2024'
                assert test_data.get('туристы') == '2 взрослый,1 дети,1 младенец, комфорт'

    @allure.id('роверить функционал фильтров ')
    @allure.story('Позитивные проверки фильтров ')
    @allure.title('Пользователь авторизовался и выбирает билет')
    @allure.description('Выполнить авторизацию ранее зарегистрированного пользователя')
    @allure.feature('AUTHORIZE')
    def auth_test(self, browser: WebDriver, test_data: DataProvider):
        index_page = IndexPage(browser)
        index_page.open()
        index_page.click_sign_in()

        team_page = TeamPage(browser)
        team_page.set_filters(test_data.get('filters'))
        team_page.login()

        with allure.step('Проверка: поле фильтры'):
            with allure.step('выбранные фильтры выделяются'):
                assert test_data.get('Выбрать пересадки и нажать несколько раз на 1 пересадку') == 'Выбрать пересадки и нажать несколько раз на 1 пересадку'
                assert test_data.get('Отменить все выбранные пересадки') == 'Отменить все выбранные пересадки'
                assert test_data.get('Фильтры можно выбрать если пользователь не авторизован') == 'Фильтры можно выбрать если пользователь не авторизован'
                assert test_data.get('Все кнопки имеют стандартный формат и размер') == 'Все кнопки имеют стандартный формат и размер'
                assert test_data.get('Все фильтры имеют свое название') == 'Все фильтры имеют свое название'
            