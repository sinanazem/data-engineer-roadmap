import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.exchange_declare(exchange="topic_logs", exchange_type="topic")

result = ch.queue_declare(queue="", exclusive=True)

qname = result.method.queue

binding_key = "#.notimportant"
ch.queue_bind(queue=qname, exchange="topic_logs", routing_key=binding_key)
    
print("waiting for receive message! press ctrl+c for stopping")

def callback(ch, method, properties, body):
    print(f"{method.routing_key}, {body}")

ch.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)

ch.start_consuming()