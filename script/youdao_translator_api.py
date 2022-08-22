## ---------------------------------------------------------------------------
## this code from official use guide:
## https://ai.youdao.com/DOCSIRMA/html/自然语言翻译/API文档/文本翻译服务/文本翻译服务-API文档.html
## must run with APP_KEY & APP_SECRET, get from here:
## https://ai.youdao.com/
## ---------------------------------------------------------------------------
# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import hashlib
from imp import reload
import json
import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = ''
APP_SECRET = ''


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def translator(q, trans_from, trans_to):
    if q:
        data = {}
        data['from'] = trans_from
        data['to'] = trans_to
        data['signType'] = 'v3'
        curtime = str(int(time.time()))
        data['curtime'] = curtime
        salt = str(uuid.uuid1())
        signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
        sign = encrypt(signStr)
        data['appKey'] = APP_KEY
        data['q'] = q
        data['salt'] = salt
        data['sign'] = sign

        response = do_request(data)
        res_json = json.loads(response.text)
        # print(res_json)
        error_code = res_json.get("errorCode")
        if error_code == "0":
            return res_json.get("translation")[0]
        else:
            return q
    else:
        return q
