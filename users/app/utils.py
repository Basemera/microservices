import os
import requests


def make_api_request(method, url, service_name):
    """Function to make http requests"""
    base_url = os.environ.get('BASE_URL', f'http://{service_name}:80')

    url = base_url + url
    response = requests.request(method=method, url=url)

    return response
