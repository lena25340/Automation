import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from api.ColumnApi import ColumnApi



@allure.epic('Тестирование функционала REST API сервиса Fun&Sun')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('API-тесты по функционал сайта')
class APITest:
    @allure.id('JM-9')
    @allure.story('Позитивные проверки Отображаются популярные  города')
    @allure.feature('CREATE')
    def create_project_test(
            self,
            project_api: ProjectApi,
            test_data: DataProvider,
            delete_utility_project: dict,
    ):
        with allure.step('Отображаются популярные  города'):
            project_title = test_data.get('project_title') + str(random.randint(0, 99999))

        with allure.step('Получить количество популярных городов'):
            len_before = len(project_api.get_projects().json()['content'])

        with allure.step('Отправить API-запрос Данные города куда взят авиабилет"{project_title}"'):
            api_response = project_api.create_project(project_title)

        with allure.step('Запросить информацию по город прибытия'):
            new_project = project_api.get_project_by_id(api_response.json()['id']).json()

        