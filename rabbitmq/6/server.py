import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost")

ch = connection.channel()

ch.queue_declare(queue="rpc_queue")

def callcack(ch, method, properties, body):
    n = int(body)
    print("processing message")
    time.sleep(4)
    resopnse = n+1
    
    
ch.basic_consume(queue="rpc_queue", on_message_callback=callback)
print("waiting for message")

ch.start_consuming()