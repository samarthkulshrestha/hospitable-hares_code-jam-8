import requests
from crypt import load_key, encrypt, decrypt
from cryptography.fernet import Fernet

base_url = 'https://hospital.divcorn.com'

def get_token_from_file():
    key = load_key()
    return decrypt("token", key)

def join():
    r = requests.get(base_url + '/join')
    data = r.json()

    token = data['token']
    with open('token', "w+") as file:
        file.write(token)

    key = load_key()
    filename = "token"

    encrypt(filename, key)

def get_posts(box_id, **kwargs):
    token = get_token_from_file()

    pload = {'box_id': box_id, "page_no": kwargs.get('page_no', '1')}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}

    r = requests.post(base_url + '/posts', data=pload, headers=headers)
    return r.json()

def post(**kwargs):
    token = get_token_from_file()

    pload = {'box_id': kwargs['box_id'], 'body': kwargs['body']}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}
    
    r = requests.post(base_url + '/post', data=pload, headers=headers)
    return r.json()

def get_boxes(**kwargs):
    token = get_token_from_file()

    pload = {"page_no": '1'}
    headers = {'Auth-Token': token, 'Content-Type': 'application/json'}

    r = requests.post(base_url + '/boxes', data=pload, headers=headers)
    return r.json()

