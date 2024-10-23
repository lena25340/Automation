import requests


class Company:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(f"{self.url}/auth/login", json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }
        BASE_HEADERS = {
        "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/company", json=company, headers=BASE_HEADERS)
        if resp.status_code != 201:
            raise Exception(f"Failed to create company: {resp.status_code}")
        return resp.json()

    def get_list_employee(self, company_id):
        params = {"company": company_id}
        resp = requests.get(
            f"{self.url}/employee",
            params=params,
            headers=self.headers
        )
        resp.raise_for_status()  
        return resp

    def get_employee_by_id(self, employee_id):
        resp = requests.get(
            f"{self.url}/employee/{employee_id}",
            headers=self.headers  
        )
        resp.raise_for_status() 
        return resp
    
    def create_employee(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }

        BASE_HEADERS = {
        "x-client-token": self.get_token()
        }
        resp = requests.post(f"{self.url}/employee", headers=BASE_HEADERS, json=employee)
        resp.raise_for_status()  
        return resp  
    
    def update_employee_info(self, isActive, last_name, email):
        user_info = {
            "lastName": last_name,
            "email": email,
            "isActive": isActive
        }

        BASE_HEADERS = {
        "x-client-token": self.get_token()
        } 
        resp = requests.patch(f"{self.url}/employee/{id_employee}", headers=BASE_HEADERS, json=user_info)
        resp.raise_for_status()  
        return resp  