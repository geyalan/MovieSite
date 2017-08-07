#coding=utf-8
import web

urls = (
    '/', 'test'
)

class test:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()