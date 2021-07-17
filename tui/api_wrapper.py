from crypt import decrypt, encrypt, load_key
from typing import Dict

import requests

base_url = 'https://hospital.divcorn.com'


def get_token_from_file() -> str:
    """Load token from file."""
    key = load_key()
    return decrypt("token", key)


def join() -> None:
    """Get token and create new user and save it to file."""
    r = requests.get(base_url + '/join')
    data = r.json()

    token = data['token']
    with open('token', "w+") as file:
        file.write(token)

    key = load_key()
    filename = "token"

    encrypt(filename, key)


def get_posts(**kwargs) -> Dict:
    """Get recent posts from api."""
    token = get_token_from_file()

    pload = {"box_id": kwargs["box_id"], "page_no": kwargs.get("page_no", "1")}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}

    r = requests.post(base_url + '/posts', json=pload, headers=headers)
    return r.json()


def post(**kwargs):
    """Create a new Post in the given Box."""
    token = get_token_from_file()

    pload = {"box_id": kwargs["box_id"], "body": kwargs["body"]}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}

    requests.post(base_url + '/post', json=pload, headers=headers)


def get_boxes(**kwargs) -> Dict:
    """Get recent boxes from the api."""
    token = get_token_from_file()

    pload = {"page_no": kwargs.get("page_no", "1")}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}

    r = requests.post(base_url + '/boxes', json=pload, headers=headers)
    return r.json()


def new_box(**kwargs) -> Dict:
    """Create a new box with the given name."""
    token = get_token_from_file()

    pload = {"name": kwargs["name"]}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}

    r = requests.post(base_url + '/new-box', json=pload, headers=headers)
    return r.json()
