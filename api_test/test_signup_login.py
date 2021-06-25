import requests
from utils import util_jwt
import json


def test_signup():
    user_info_leader_1 = {
        "username": "abcd",
        "realname": "小陈",
        "password": "12345678",
        "identify": "测试领导"
    }

    jwt_info = {
        "jwt_info": util_jwt.jwt_encoding(user_info_leader_1)
    }

    re = requests.post("http://localhost:8000/users/signup/", data=json.dumps(jwt_info))
    print(re.text)
    # print(re.json()['jwt_info'])


if __name__ == '__main__':
    test_signup()
