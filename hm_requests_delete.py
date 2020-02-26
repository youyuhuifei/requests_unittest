"""
    目标：requests库put方法使用

    案例：新增学院  修改名称


    响应：
        1、响应对象.json()

"""


# 1、导包
import requests
import json
url = "http://www."
r = requests.delete(url)

# 4、获取响应状态码
print(r.status_code)