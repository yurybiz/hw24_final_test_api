import requests
from endpoints.endpoint import Endpoint
import allure


class Memes(Endpoint):

    @allure.step('View all memes')
    def memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}meme',
            headers=headers
        )
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
            except ValueError:
                self.json = None
        else:
            self.json = None

        return self.response