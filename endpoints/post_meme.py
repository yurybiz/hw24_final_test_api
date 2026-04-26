import requests
from endpoints.endpoint import Endpoint
import allure


class CreateMeme(Endpoint):

    @allure.step('Create new meme')
    def create_new_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}meme',
            json=payload,
            headers=headers
        )
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
                print(self.json)
            except ValueError:
                print("\nResponse is not in JSON format.")
                self.json = None
        else:
            print(f"\nError {self.response.status_code}:\n{self.response.text}")
            self.json = None
        return self.response