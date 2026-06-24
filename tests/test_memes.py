import pytest


def test_token_is_alive(get_token, post_meme_authorize):
    user = 'ytest'
    get_token.get_token()
    if get_token.response.status_code == 404:
        data = {"name": f'{user}'}
        post_meme_authorize.authorize(data)
        post_meme_authorize.check_that_status_is_200()
        post_meme_authorize.check_response_field('name', data['name'])
        post_meme_authorize.check_token_is_not_none()
    else:
        get_token.check_status_code(200)
        get_token.check_response_user_the_same(user)


TEST_DATA_POST = [
    {
        "id": None,
        "text": "Ytest meme about python learning",
        "url": "https://prnt.sc/Xy3gJxwAE0zN",
        "info": {
            "colors": [
                "blue",
                "yellow",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "python",
            "learning"
        ]
    }
]


@pytest.mark.parametrize('data', TEST_DATA_POST)
def test_get_memes(meme, get_memes):
    get_memes.memes()
    get_memes.check_status_code(200)


@pytest.mark.parametrize('data', TEST_DATA_POST)
def test_post_meme(meme, post_meme, data):
    post_meme.check_status_code(200)
    post_meme.check_response_field('text', data['text'])
    post_meme.check_response_field('url', data['url'])
    post_meme.check_response_field('info', data['info'])
    post_meme.check_response_field('tags', data['tags'])


INVALID_DATA_POST = [
    {
        "id": None,
        "text": None,
        "url": "https://prnt.sc/Xy3gJxwAE0zN",
        "info": {
            "colors": [
                "blue",
                "yellow",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "python",
            "learning"
        ]
    }, # text is None
    {
        "id": None,
        "text": "Ytest meme about python learning",
        "url": None,
        "info": {
            "colors": [
                "blue",
                "yellow",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": [
            "fun",
            "python",
            "learning"
        ]
    }, # url is None
    {
        "id": None,
        "text": "Ytest meme about python learning",
        "url": "https://prnt.sc/Xy3gJxwAE0zN",
        "info": None,
        "tags": [
            "fun",
            "python",
            "learning"
        ]
    }, # info is None
    {
        "id": None,
        "text": "Ytest meme about python learning",
        "url": "https://prnt.sc/Xy3gJxwAE0zN",
        "info": {
            "colors": [
                "blue",
                "yellow",
                "black",
                "white"
            ],
            "objects": [
                "picture",
                "text"
            ]
        },
        "tags": None
    } # tags is None
]

@pytest.mark.parametrize('data', INVALID_DATA_POST)
def test_post_invalid_meme(post_meme,data):
    post_meme.create_new_meme(data)
    post_meme.check_status_code(400)


@pytest.mark.parametrize('data', TEST_DATA_POST)
def test_get_meme(meme, get_meme, data):
    mem = get_meme.meme(meme)
    get_meme.check_id(mem.json()['id'], meme)
    get_meme.check_status_code(200)


def test_get_invalid_meme(get_meme):
    invalid_id = '39ewuih'
    get_meme.meme(invalid_id)
    get_meme.check_status_code(404)


TEST_DATA_PUT = [
    {
        "text": "Ytest meme about python learning - PUT",
        "url": "https://prnt.sc/Xy3gJxwAE0zN/?utm_add=PUT",
        "info": {
            "colors": [
                "blue",
                "black",
                "white",
                "red"
            ],
            "objects": [
                "image",
                "description"
            ]
        },
        "tags": [
            "fun",
            "python",
            "c++"
        ]
    }
]


@pytest.mark.parametrize('data', TEST_DATA_POST)
@pytest.mark.parametrize('data_put', TEST_DATA_PUT)
def test_put_meme(meme, put_meme, data, data_put):
    update_data = {
        'id': meme,
        **data_put
    }
    put_meme.update_meme(update_data, meme)
    put_meme.check_status_code(200)
    put_meme.check_response_field('text', update_data['text'])
    put_meme.check_response_field('url', update_data['url'])
    put_meme.check_response_field('info', update_data['info'])
    put_meme.check_response_field('tags', update_data['tags'])


@pytest.mark.parametrize('data', TEST_DATA_POST)
@pytest.mark.parametrize('data_put', TEST_DATA_PUT)
def test_put_invalid_meme_id_none_json(meme, put_meme, data, data_put):
    update_data = {
        'id': None,
        **data_put
    }
    put_meme.update_meme(update_data, meme)
    put_meme.check_status_code(400)


@pytest.mark.parametrize('data', TEST_DATA_POST)
@pytest.mark.parametrize('data_put', TEST_DATA_PUT)
def test_put_invalid_meme_id_none_url(meme, put_meme, data, data_put):
    update_data = {
        'id': meme,
        **data_put
    }
    put_meme.update_meme(update_data, None)
    put_meme.check_status_code(404)

INVALID_DATA_PUT = [
    {
        "text": None,
        "url": "https://prnt.sc/Xy3gJxwAE0zN/?utm_add=PUT",
        "info": {
            "colors": [
                "blue",
                "black",
                "white",
                "red"
            ],
            "objects": [
                "image",
                "description"
            ]
        },
        "tags": [
            "fun",
            "python",
            "c++"
        ]
    }, # text is None
    {
        "text": "Ytest meme about python learning - PUT",
        "url": None,
        "info": {
            "colors": [
                "blue",
                "black",
                "white",
                "red"
            ],
            "objects": [
                "image",
                "description"
            ]
        },
        "tags": [
            "fun",
            "python",
            "c++"
        ]
    }, # url is None
    {
        "text": "Ytest meme about python learning - PUT",
        "url": "https://prnt.sc/Xy3gJxwAE0zN/?utm_add=PUT",
        "info": None,
        "tags": [
            "fun",
            "python",
            "c++"
        ]
    }, # info is None
    {
        "text": "Ytest meme about python learning - PUT",
        "url": "https://prnt.sc/Xy3gJxwAE0zN/?utm_add=PUT",
        "info": {
            "colors": [
                "blue",
                "black",
                "white",
                "red"
            ],
            "objects": [
                "image",
                "description"
            ]
        },
        "tags": None
    } # tags is None
]

@pytest.mark.parametrize('data', TEST_DATA_POST)
@pytest.mark.parametrize('data_put', INVALID_DATA_PUT)
def test_put_invalid_meme(meme, put_meme, data, data_put):
    update_data = {
        'id': meme,
        **data_put
    }
    put_meme.update_meme(update_data, meme)
    put_meme.check_status_code(400)


@pytest.mark.parametrize('data', TEST_DATA_POST)
def test_delete_meme(meme, delete_meme, get_memes, data):
    delete_meme.delete_meme(meme)
    delete_meme.check_status_code(200)
    get_memes.memes()
    get_memes.check_that_item_is_deleted(meme)


def test_delete_invalid_meme(delete_meme):
    invalid_id = '39ewuih'
    delete_meme.delete_meme(invalid_id)
    delete_meme.check_status_code(404)
