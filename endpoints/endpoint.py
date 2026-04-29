import allure
import os
from dotenv import load_dotenv


class Endpoint:
    load_dotenv()
    token = os.getenv('TOKEN')
    url = 'http://memesapi.course.qa-practice.com/'
    response = None
    json = None
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, but got {self.response.status_code}"

    @allure.step('Check that response is 404')
    def check_that_status_is_404(self):
        assert self.response.status_code == 404, f"Expected status code 404, but got {self.response.status_code}"

    @allure.step('Check that response is 404')
    def check_that_status_is_400(self):
        assert self.response.status_code == 400, f"Expected status code 400, but got {self.response.status_code}"

    @allure.step('Check the name is the same as sent')
    def check_response_user_is_correct(self, expected_user):
        assert self.json['user'] == expected_user, f"Expected user {expected_user}, but got {self.json['user']}"

    @allure.step('Check the token is not None')
    def check_token_is_not_none(self):
        assert self.json['token'] is not None, "Token should not be None"
        assert self.json['token'] != "", "Token should not be empty"

    @allure.step('Check the name is the same')
    def check_response_user_the_same(self, expected_user):
        assert self.json == f'Token is alive. Username is {expected_user}', f"Expected 'Token is alive. Username is {expected_user}', but got '{self.json}'"

    @allure.step('Check the text in data is the same as sent')
    def check_response_text_in_data_is_correct(self, expected_text):
        assert self.response.json()['text'] == expected_text, f"Expected text in data {expected_text}, but got {self.response.json()['text']}"

    @allure.step('Check the url in data is the same as sent')
    def check_response_url_in_data_is_correct(self, expected_url):
        assert self.response.json()[
                   'url'] == expected_url, f"Expected url in data {expected_url}, but got {self.response.json()['url']}"

    @allure.step('Check the info in data is the same as sent')
    def check_response_info_in_data_is_correct(self, expected_info):
        assert self.response.json()[
                   'info'] == expected_info, f"Expected info in data {expected_info}, but got {self.response.json()['info']}"

    @allure.step('Check the tags in data is the same as sent')
    def check_response_tags_in_data_is_correct(self, expected_tags):
        assert self.response.json()[
                   'tags'] == expected_tags, f"Expected tags in data {expected_tags}, but got {self.response.json()['tags']}"