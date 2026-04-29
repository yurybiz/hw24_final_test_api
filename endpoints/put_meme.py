import requests
from endpoints.endpoint import Endpoint
import allure


class UpdateMeme(Endpoint):

    @allure.step('Update meme')
    def update_meme(self, payload, id_meme, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}meme/{id_meme}',
            json=payload,
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
