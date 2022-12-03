import os
import sys
from typing import Union
import psycopg2
import psycopg2.extras
import json
from fastapi import FastAPI
import pika

app = FastAPI()




@app.get("/")
def get_root():
    return {"Service":"DB"}

def main():
    connection = pika.BlockingConnection(pika.URLParameters("amqp://test:test@rabbitmq/")) #pika.ConnectionParameters("amqp://test:test@rabbitmq/"))
    channel = connection.channel()

    channel.queue_declare(queue='ticket')

    def callback(ch, method, properties, body):
        #print(" [x] Received %r" % body)
        print("RECEIVED MESSAGE: ",body.decode('utf-8').replace(": ",':"').replace(",",'",').replace("}",'"}'))
        replaced = body.decode('utf-8').replace(": ", ':"').replace(",", '",').replace("}", '"}')
        js = json.loads(replaced)
        conn = psycopg2.connect(database="postgres", user="postgres", password="test", host="localhost", port=5432)
        cur = conn.cursor()
        query = "INSERT INTO tickets (name, secondname, patronymic, phone, text) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (js.get("name"), js.get("secondname"), js.get("patronymic"), js.get("phone"), js.get("text")))
        conn.commit()


    channel.basic_consume(queue='ticket', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

