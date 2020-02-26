"""
    目标：requests库post方法使用

    案例：新增学院

    参数：
        1、json: 传入json字符串
        2、headers 传入请求信息内容

    响应：
        1、响应对象.json()

"""

# 1、导包
import requests

# 2、调用post
# 请求URL
url = "http://"
# 请求headers
headers = {"Content_Type": "application/json"}
# 请求json
data = {}  #从接口文档获取
r = requests.post(url, json=data, headers=headers)

# 3、获取响应对象
print(r.json())

# 4、获取响应状态码
print(r.status_code)