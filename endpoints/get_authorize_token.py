import requests
from endpoints.endpoint import Endpoint
import allure


class Token(Endpoint):

    @allure.step('Get token')
    def get_token(self):
        self.response = requests.get(
            f'{self.url}authorize/{self.token}',
            headers={'Content-Type': 'application/json'}
        )
        self.json = self.response.text
        return self.response
