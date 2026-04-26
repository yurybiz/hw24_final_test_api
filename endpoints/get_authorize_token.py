import requests
from endpoints.endpoint import Endpoint


class Token(Endpoint):

    def get_token(self):
        self.response = requests.get(
            f'{self.url}authorize/{self.token}',
            headers={'Content-Type': 'application/json'}
        )
        print(f'\n{self.response.text}')
        self.json = self.response.text
        return self.response
