import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="direct_logs", exchange_type="direct")

messages = {
    "info": "this is INFO message",
    "warning": "this is WARNING message",
    "error": "this is error message",
}

for k,v in messages.items():
    ch.basic_publish(exchange="direct_logs", routing_key=k, body=v)

print("message sent")

connection.close()