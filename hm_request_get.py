"""
get 请求方法演练
案例：http://www.baidu.com
请求：
    请求方法：get
响应：
    响应对象.url  获取请求URL
    响应对象.status.code   获取响应状态吗
    响应对象.text  以文本形式显示相应内容

"""

# 1、导包
import requests

# 2、调用get
url = "http://www.baidu.com"
respond = requests.get(url)  # respond 为响应对象
# 3、获取请求URL
print("请求URL：", respond.url)
# 4、获取相应状态码
print("响应状态码：", respond.status_code)

# 5、获取响应信息
print("文本响应信息", respond.text)
