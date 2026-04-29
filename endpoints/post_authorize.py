from pathlib import Path
from dotenv import set_key, load_dotenv
import requests
from endpoints.endpoint import Endpoint
import allure


class Authorize(Endpoint):

    @allure.step('Post token')
    def authorize(self, payload):
        self.response = requests.post(
            url=f'{self.url}authorize',
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        self.json = self.response.json()
        self.token = self.json.get('token')
        if self.token:
            env_path = Path('.') / '.env'
            if not env_path.exists():
                env_path.write_text('')
            set_key(str(env_path), 'TOKEN', self.token)
        load_dotenv(override=True)
        return self.response
