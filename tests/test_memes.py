import pytest


LOGIN_DATA = [{"name": "ytest"}]


@pytest.mark.parametrize('data', LOGIN_DATA)
def test_post_authorize(post_meme_authorize, data):
    post_meme_authorize.authorize(data)
    post_meme_authorize.check_that_status_is_200()
    post_meme_authorize.check_response_user_is_correct(data['name'])


def test_get_token(get_token):
    get_token.get_token()
    get_token.check_that_status_is_200()


def test_get_memes(check_token_is_alive, get_memes):
    get_memes.memes()
    get_memes.check_that_status_is_200()


