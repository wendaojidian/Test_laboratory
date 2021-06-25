import jwt
from Test_laboratory.settings import SECRET_KEY
from jwt import exceptions


def jwt_encoding(payload):
    SALT = SECRET_KEY
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    return jwt.encode(payload=payload, key=SALT, algorithm="HS256", headers=headers).encode('utf-8').decode('utf-8')


def jwt_decoding(token):
    SALT = SECRET_KEY

    payload = None
    msg = None
    try:
        payload = jwt.decode(token, SALT, True)
        msg = "token认证成功"
    except exceptions.ExpiredSignatureError:
        msg = "超时错误，token已失效"
    except jwt.DecodeError:
        msg = "token认证失败"
    except jwt.InvalidTokenError:
        msg = "非法token"
    return {"payload": payload, "msg": msg}


"""
try:
        # 从token中获取payload【不校验合法性】
        # unverified_payload = jwt.decode(token, None, False)
        # print(unverified_payload)
        # 从token中获取payload【校验合法性】
        verified_payload = jwt.decode(token, SALT, True)
        return verified_payload
    except exceptions.ExpiredSignatureError:
        print('token已失效')
    except jwt.DecodeError:
        print('token认证失败')
    except jwt.InvalidTokenError:
        print('非法的token')

"""