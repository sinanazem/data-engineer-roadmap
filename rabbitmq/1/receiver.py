import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch2 = connection.channel()

ch2.queue_declare(queue="hello")

def callback(ch, method, properties, body):
    print(f" Received: {body}")

ch2.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print("waiting for message for wxit please ctrl+c: ")
ch2.start_consuming()