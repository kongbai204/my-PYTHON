# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回网页内容
print(x.text)
print(x.status_code)  # 获取响应状态码
print(x.headers)  # 获取响应头
print(x.content)  # 获取响应内容