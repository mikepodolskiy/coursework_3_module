# import required modules
from app import app

# set variables
# variable for quantity of tests for post id
api_post_id_test_count = 16

# list of keys, used in initial file
allowed_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]


def test_app_api_posts():
    """
    getting api using request test.client().get, transforming data
    checking type of data
    searching for keys in data, forming list of received keys
    search through list of received keys - checking if used the same keys
    """
    response = app.test_client().get('/api/posts/')
    data = response.json
    assert type(data) == list, 'Wrong received data type'
    received_keys = []
    for element in data:
        received_keys.append(list(element.keys()))
    for new_element in received_keys:
        assert set(new_element) == set(allowed_keys), 'Wrong received data format'


def test_app_api_posts_id():
    """
    creating path for api request, using number of tests to run
    getting api using request test.client().get, transforming data
    checking type of data
    forming list of requested dicts, and checking keys the same as in
    test_app_api_posts()
    """
    path = f'/api/posts/{api_post_id_test_count}'
    received_keys = []
    list_of_test_responses = []
    for test in range(1, api_post_id_test_count):
        response = app.test_client().get(path)
        data = response.json
        list_of_test_responses.append(data)
        assert type(data) == dict, 'Wrong received data type'
    for element in list_of_test_responses:
        received_keys.append(list(element.keys()))
    for new_element in received_keys:
        assert set(new_element) == set(allowed_keys), 'Wrong received data format'
