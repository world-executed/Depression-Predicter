# -*- coding:utf-8 -*-
# @Time    :2020/9/1 0:30
# @Author  :Benjamin
# @File    :predict.py

import requests
import json

# 填入下面四个信息
API_KEY = 'HBTnQr8eDxZik0oXMC1f5W2g'
SECRET_KEY = 'gXzfpmSiaSOSrDSKX0aNbt3GWcrAzXeX'
Request_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/mmd_hc'

mmd_threshold = 0.8
MMD_scores = []
host = 'https://aip.baidubce.com/oauth/2.0/token'
data = {
    'grant_type': 'client_credentials',
    'client_id': API_KEY,
    'client_secret': SECRET_KEY
}
response = requests.post(host, data=data)
token = response.json()["access_token"]
url = Request_url + "?access_token=" + token
headers = {'Content-Type': 'application/json'}


def predict(wav_b64):
    params = {
        "sound": wav_b64,
        "top_num": 2
    }
    response = requests.post(url, data=json.dumps(params), headers=headers).json()

    if 'results' in response:
        result = response['results'][0]
        print(result)
        if result['name'] == 'HC':
            MMD_scores.append(1 - float(result['score']))
        elif result['name'] == 'MMD':
            MMD_scores.append(float(result['score']))
        msg="预测结果为：%s  概率为：%.3f。" % ('正常' if result['name'] == 'SC' else '抑郁症', result['score'])

    elif 'error_code' in response:
        msg="数据有误！"

    return msg

def final_evaluate():
    if len(MMD_scores):
        score = sum(MMD_scores) / len(MMD_scores)

        result={
            "score":score,
            "num":len(MMD_scores)
        }
        return result
    else:
        return None
