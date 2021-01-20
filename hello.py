# hello.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 基本用法
    #return [b'<h1>Hello, web!</h1>']
    # 入门用法
    #body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

    #return [body.encode('utf-8')]
    
    # 进阶用法
    url = '%s' % (environ['PATH_INFO'][1:] or 'index.html')
    f = open(url, 'rb') 
    body = f.read()
    f.close

    return [body]