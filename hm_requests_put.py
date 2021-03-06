"""
    目标：requests库put方法使用

    案例：新增学院  修改名称

    将字典对象转换为json字符串
        1、导入json
        2.调用json下方法dumps(dict)
    响应对象text与json区别


    参数：
        1、json: 传入json字符串
        2、headers 传入请求信息内容

    响应：
        1、响应对象.json()

"""


# 1、导包
import requests
import json
# 2、调用post
# 请求URL
url = "http://"
# 请求headers
headers = {"Content_Type": "application/json"}
# 请求json
data = {}  #从接口文档获取
# 使用json方式来新增学院
# r = requests.post(url, json=data, headers=headers)
# 使用data 方式新hm_requests_put.py增学院
# r = requests.post(url, data=data, headers=headers)  #失败

# 将字典对象转为json字符串
r = requests.put(url, data=json.dumps(data), headers=headers)

# 3、获取响应对象
# print(r.json())
# json 返回为字典
r_json = r.json()
#text 返回为字符串
r_text = r.text
# 4、获取响应状态码
print(r.status_code)