import requests
from endpoints.endpoint import Endpoint


class Authorize(Endpoint):

    def authorize(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}authorize',
            json=payload,
            headers=headers
        )
