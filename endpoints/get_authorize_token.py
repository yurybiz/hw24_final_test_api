import requests
from endpoints.endpoint import Endpoint
import allure
import os
from dotenv import load_dotenv


class Token(Endpoint):

    @allure.step('Get token')
    def get_token(self):
        load_dotenv()
        token = os.getenv('TOKEN')
        self.response = requests.get(
            # f'{self.url}authorize/{self.token}',
            url=f'{self.url}authorize/{token}',
            headers={'Content-Type': 'application/json'}
        )
        self.json = self.response.text
        return self.response
