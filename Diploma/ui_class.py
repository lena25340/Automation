import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ProjectPage:
    """Класс предоставляет методы для выполнения UI-тестов на странице авиокомпании"""
    
    __driver: WebDriver
    __timeout: int

    def __init__(self, driver: WebDriver) -> None:
     
        
        self.__driver = driver
        self.__timeout = WebDriverWait().get_int('ui', 'timeout')
        
    @allure.step('[UI] Авторизация {column_title}')           
    def get_task_titles(self, column_title: str) -> list[str]:
       