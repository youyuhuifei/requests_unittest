"""
get 请求方法演练
案例：
    http://www.baidu.com?id=1001
    http://www.baidu.com?id=1001,1002
    http://www.baidu.com?id=1001&kw=北京
请求：
    请求方法：get
    参数：
        params：字典或字符串 推荐使用字典
响应：
    响应对象.url  获取请求URL
    响应对象.status.code   获取响应状态吗
    响应对象.text  以文本形式显示相应内容
"""

# 1、导包
import requests

# 2、调用get
url = "http://www.baidu.com"
# 不推荐写法
# url = "http://www.baidu.com?id=1001"
# 案例1  定义字典
# params = {"id": 1001}
# 案例1字符串形式编写
# respond = requests.get(url, params="id=1001")  # respond 为响应对象

# 案例2
# params = {"id": "1001,1002"}  #%2C 为,
# 案例3
params = {"id": 1001, "kw": "beijng"}  #多个键值对
respond = requests.get(url, params=params)  # respond 为响应对象
# 3、获取请求URL
print("请求URL：", respond.url)
# 4、获取相应状态码
print("响应状态码：", respond.status_code)

# 5、获取响应信息
print("文本响应信息", respond.text)
