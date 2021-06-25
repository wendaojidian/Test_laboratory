import requests
import pprint

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)


def test_signup():
    user_info_leader_1 = {
        "username": "abcd",
        "realname": "小陈",
        "password": "12345678",
        "identify": "测试领导"
    }

    re = requests.post("http://localhost:8000/users/signup/", json=user_info_leader_1)
    print(re.json())


if __name__ == '__main__':
    test_signup()

"""
import  requests,pprint

# 构建添加 客户信息的 消息体，是json格式
payload = {
    "action":"add_customer",
    "data":{
        "name":"武汉市桥西医院",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}

# 发送请求给web服务
response = requests.post('http://localhost/api/mgr/customers',
              json=payload)

pprint.pprint(response.json())

# 构建查看 客户信息的消息体
response = requests.get('http://localhost/api/mgr/customers?action=list_customer')

# 发送请求给web服务
pprint.pprint(response.json())
"""
