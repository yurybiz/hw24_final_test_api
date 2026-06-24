import allure
import os
from dotenv import load_dotenv


class Endpoint:
    load_dotenv(override=True)
    token = os.getenv('TOKEN')
    url = 'http://memesapi.course.qa-practice.com/'
    response = None
    json = None
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    @allure.step('Check status code')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code, \
            f"Expected status code {status_code}, but got {self.response.status_code}"

    @allure.step('Check response field')
    def check_response_field(self, field_name, expected_value):
        assert self.json[field_name] == expected_value, f"Expected value {expected_value}, but got {self.json[field_name]}"

    @allure.step('Check id')
    def check_id(self, real_id, expected_id):
        assert real_id == expected_id, f"Expected value {expected_id}, but got {real_id}"

    @allure.step('Check the token is not None')
    def check_token_is_not_none(self):
        assert self.json['token'] is not None, "Token should not be None"
        assert self.json['token'] != "", "Token should not be empty"

    @allure.step('Check the name is the same')
    def check_response_user_the_same(self, expected_user):
        assert self.json == f'Token is alive. Username is {expected_user}', f"Expected 'Token is alive. Username is {expected_user}', but got '{self.json}'"

    # @allure.step('Check that id is exist')
    # def check_that_item_is_exist(self, id):
    #     data = self.response.json()["data"]
    #     assert any(item["id"] == id for item in data), \
    #         f"ID '{id}' not found in response, but it should exist"

    @allure.step('Check that id is deleted')
    def check_that_item_is_deleted(self, id):
        data = self.response.json()["data"]
        assert all(item["id"] != id for item in data), \
            f"ID '{id}' found in response, but it should not exist"