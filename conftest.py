import pytest
from endpoints.post_authorize import Authorize


@pytest.fixture()
def post_meme_authorize():
    return Authorize()
