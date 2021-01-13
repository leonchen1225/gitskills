# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

#仅通过WSGI去开发web应用，还是会过于底层，于是又发展出了各种框架
#例如Flask、Django等,它们又在WSGI之上再抽象一层，让python更方便的关注于处理业务