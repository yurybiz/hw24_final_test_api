import requests
from endpoints.endpoint import Endpoint
import allure


class Meme(Endpoint):

    @allure.step('Get meme')
    def meme(self, id_meme, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}meme/{id_meme}',
            headers=headers
        )
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
                print(self.json)
            except ValueError:
                print("\nResponse is not in JSON format.")
                self.json = None
                print(self.response.text)
        else:
            print(f"\nError {self.response.status_code}:\n{self.response.text}")
            self.json = None
        self.json = self.response.text
        return self.response