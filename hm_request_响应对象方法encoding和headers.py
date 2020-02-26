"""
    目标：响应对象常用方法
        1、encoding
            获取请求编码
            设置响应编码
        2、headers
            获取响应信息头信息
        3、cookies
            获取响应cookies信息
        4、content
            以字节码形式获取响应信息  图片 视频 多媒体格式
        https://www.baidu.com/img/PCpad_bc531b595cf1e37c3907d14b69e3a2dd.png

"""

# 1、导包
import requests

# 2、调用get
url = "http://www.baidu.com"
url_img = "https://www.baidu.com/img/PCpad_bc531b595cf1e37c3907d14b69e3a2dd.png"
r = respond = requests.get(url)  # respond 为响应对象
# 3、查看默认请求编码
print(r.encoding)
# 设置编码格式
r.encoding = "utf-8"
# 查看响应内容
print(r.text)

# 5、查看响应信息头headers  headers信息比较重要，
# 项目工作中一般服务器返回的token session相关信息在header中
print(r.headers)

# 获取响应cookies信息 返回字典对象
print(r.cookies)
# 通过健名或cookies值
print(r.cookies["BDORZ"])

# 以字节码形式解析图片
r = requests.get(url_img)
print(r.content)

# 将图片写入当前目录baidu.png
with open("./baidu.png", "wb") as f:
    f.write(r.content)
