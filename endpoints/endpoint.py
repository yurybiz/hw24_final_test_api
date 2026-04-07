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

    @allure.step('Check the name is the same as sent')
    def check_response_user_is_correct(self, expected_user):
        assert self.json['user'] == expected_user, f"Expected user {expected_user}, but got {self.json['user']}"
