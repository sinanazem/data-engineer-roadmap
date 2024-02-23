import pika
import uuid

class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.qname = result.method.queue
        
        
    def call(self, n):
        self.response = None 
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange="", routing_key="rpc_queue",
        properties=pika.BasicProperties(reply_to=self.qname, correlation_id=self.corr_id, body=str(n))
        
    

send = Sender()
send.call(30)