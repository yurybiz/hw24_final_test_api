import pytest
from endpoints.delete_meme import DeleteMeme
from endpoints.get_memes import Memes
from endpoints.post_authorize import Authorize
from endpoints.get_authorize_token import Token
from endpoints.post_meme import CreateMeme
from endpoints.get_meme import Meme
from endpoints.put_meme import UpdateMeme


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
def get_meme():
    return Meme()


@pytest.fixture()
def post_meme():
    return CreateMeme()


@pytest.fixture()
def put_meme():
    return UpdateMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def meme(post_meme, delete_meme, data):
    new_meme = post_meme.create_new_meme(payload=data)

    if new_meme.status_code == 200:
        try:
            meme_id = new_meme.json()['id']
            yield meme_id
            delete_meme.delete_meme(meme_id)
        except ValueError:
            pytest.fail("Response is not in JSON format")
    else:
        pytest.fail(f"Failed to create meme. Status {new_meme.status_code}: {new_meme.text}")
