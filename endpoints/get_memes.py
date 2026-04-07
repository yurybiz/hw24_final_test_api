import requests

from endpoints.endpoint import Endpoint


class Memes(Endpoint):

    def memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}meme',
            headers=headers
        )
        # self.json = self.response.json()
        # print(f'\n{self.json}')
        # return self.json
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
                print(f'\n{self.json}')
            except ValueError:
                print("\nError: Response is not in JSON format.")
                self.json = None
        else:
            print(f"\nError {self.response.status_code}:\n{self.response.text}")
            self.json = None

        return self.response