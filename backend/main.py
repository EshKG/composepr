import os

import json
import datetime
import tornado.httpserver
import tornado.ioloop
import tornado.web

import pika
import sys








#print(" [x] Sent %r:%r" % (severity, message))




'''conn = psycopg2.connect( database="postgres", user="postgres", password="test", host="localhost", port=5432)
cur = conn.cursor()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('./templates/index.html')


class AboutHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('about.html')
'''


class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('ticket.html')

    def post(self):
        name = self.get_argument('name')
        secondname = self.get_argument('secondname')
        patronymic = self.get_argument('patronymic')
        phone = self.get_argument('phone')
        text = self.get_argument('text')

        #created = datetime.datetime.now()

        #query = "INSERT INTO tickets (name, secondname, patronymic,phone, text) VALUES (%s, %s, %s,%s, %s)"
     #cur.execute(query, (name, secondname, patronymic, phone, text))
      #  conn.commit()

       # ssl_options = pika.SSLOptions(context, "rabbitmq-node-name")
        connection = pika.BlockingConnection(
           # pika.ConnectionParameters("amqp://test:test@rabbitmq/"))
            pika.URLParameters("amqp://test:test@rabbitmq/"))
        channel = connection.channel()

        channel.queue_declare(queue='ticket')

        #js = '{"Имя": {0}, "Фамилия": {1}, "Отчетсво": {2}, "Номер телефона": {3}, "Обращение": {4}}'.format(str(name), secondname, patronymic, phone, text)
        #js = '{"a":"b"}'
        js = '{"name": '  + str(name) + ', "secondname": ' + secondname + ', "patronymic": ' + patronymic + ', "phone": ' + phone + ', "text": ' + text + '}'

        channel.basic_publish(exchange='', routing_key='ticket', #properties=pika.spec.BasicProperties(content_type='application/json',content_encoding="utf-8"),
                              body=bytes(js.encode(encoding='utf-8')))
        print(" [x] Отправлено обращение")
        connection.close()


        self.write('Submitted successfully')


def main():
    settings = dict(
        cookie_secret=str(os.urandom(45)),
        #template_path=os.path.join(os.path.dirname(__file__), "frontend"),
        template_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"frontend"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        autoreload=True,
        gzip=True,
        debug=True,
        #login_url='/login',
        autoescape=None
    )

    application = tornado.web.Application([
        #(r"/", MainHandler),
       # (r"/about", AboutHandler),
        (r"/", ContactHandler)
    ], **settings)

    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 80))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

