import pytest
from endpoints.get_memes import Memes
from endpoints.post_authorize import Authorize
from endpoints.get_authorize_token import Token
from dotenv import load_dotenv


@pytest.fixture()
def post_meme_authorize():
    return Authorize()


@pytest.fixture()
def get_token():
    return Token()


@pytest.fixture()
def get_memes():
    return Memes()


@pytest.fixture()
def check_token_is_alive(get_token, post_meme_authorize):
    response = get_token.get_token()
    if response.status_code == 404:
        post_meme_authorize.authorize(payload={"name": "ytest"})
        load_dotenv(override=True)
    else:
        return