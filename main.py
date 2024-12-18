import requests
import os 

URL = 'https://app.kajabi.com/api/v1/oauth/token'
USERNAME = "soma@cerveauetpsychologie.com"
PASSWORD = "W?wQWrm6%??6Vzq"
def get_token():
    if os.path.exists('token.txt'):
        print('Token file already exists, returning token')
        with open('token.txt', 'r') as file:
            return file.read()
    else:
        print('No token found, getting token from server')
        response = requests.post(URL, data={
            'username': USERNAME,
            'password': PASSWORD,
        })
        token = response.json()['access_token']
        with open('token.txt', 'w') as file:
            file.write(token)
        return token


token = get_token()