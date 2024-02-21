import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="topic_logs", exchange_type="topic")

messages = {
    "error.warning.important": "this is important message",
    "error.debug.notimportant": "this is notimportant message",
}

for k,v in messages.items():
    ch.basic_publish(exchange="topic_logs", routing_key=k, body=v)

print("message sent")

connection.close()
