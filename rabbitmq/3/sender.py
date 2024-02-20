import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

ch = connection.channel()

ch.exchange_declare(exchange="logs", exchange_type="fanout")

ch.basic_publish(exchange="logs", routing_key="", body="this is a testing fanout")

print("message sent!")

connection.close()

