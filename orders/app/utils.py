import os
import requests
import timeout_decorator

class TimeoutError(Exception):
    pass

@timeout_decorator.timeout(5, timeout_exception=TimeoutError, use_signals=False)
def make_api_request(method, url, service_name):
    """Function to make http requests"""
    base_url = os.environ.get('BASE_URL', f'http://{service_name}:5000')

    url = base_url + url
    response = requests.request(method=method, url=url)

    return response
