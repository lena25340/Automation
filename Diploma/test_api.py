import allure
import requests


class EmployeesApi:
    def __init__(self, url):
        self.url = url

    @allure.step("api.Отображаются популярные города  {name}:{description}")
    def create_company(self, name: str, description=""):
        company = {'name': name, 'description': description}
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(
            self.url + '/company', json=company, headers=my_headers
        )
        return resp.json()

    @allure.step("api.Данные города куда взят авиабилет{id}")
    def get_company(self, id: int):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    @allure.step("api.Город прибытия {id}")
    def get_employee(self, id: int):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()
