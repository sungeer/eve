import requests


def get_access_token(phone_number, password):
    url = 'http://127.0.0.1:8000/user/get-access-token'
    data = {
        'phone_number': phone_number,
        'password': password
    }
    response = requests.post(url, json=data)
    data = response.json()
    print(data)


if __name__ == '__main__':
    phone_number = '18112286003'
    password = 'SM!9$5&3'
    access_token = get_access_token(phone_number, password)
    print(access_token)
