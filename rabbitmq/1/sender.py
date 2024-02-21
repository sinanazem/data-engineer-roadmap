import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host=""))

ch1 = connection.channel()

ch1.queue_declare("hello")
ch1.basic_publish(exchange="", routing_key="hello", body="hello world")
print("message sent!")

connection.close()
