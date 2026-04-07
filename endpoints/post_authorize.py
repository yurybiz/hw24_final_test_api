from pathlib import Path
from dotenv import set_key, load_dotenv
import requests
from endpoints.endpoint import Endpoint


class Authorize(Endpoint):


    def authorize(self, payload):
        self.response = requests.post(
            url=f'{self.url}authorize',
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        self.json = self.response.json()
        self.token = self.json.get('token')
        print(f'\n{self.token}')

        if self.token:
            # путь к .env (в корне проекта)
            env_path = Path('.') / '.env'
            # если файла .env ещё нет, создаём
            if not env_path.exists():
                env_path.write_text('')  # создаёт пустой файл

            # используем set_key из python-dotenv чтобы записать/обновить значение
            set_key(str(env_path), 'TOKEN', self.token)
            # альтернативно можно открыть файл и дописать вручную:
            # with open(env_path, 'a', encoding='utf-8') as f:
            #     f.write(f'\nTOKEN={self.token}\n')
        load_dotenv(override=True)
        return self.response
