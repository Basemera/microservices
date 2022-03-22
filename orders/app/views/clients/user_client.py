from ...utils import make_api_request


def get_user(user_id):
    """
    Makes an http call to the User service to get user details
    Parameters
    ----------
    user_id: str
        The id of the user whose details are to be returned
    """
    client_response = make_api_request(
        'GET', f'/users/{user_id}',
        'cusers'
        )
    if client_response.status_code != 200:
        response = str(client_response)
    else:
        response = client_response.json()
    return {
        'response': response,
        'status': client_response.status_code
    }
