from celery import Celery
import time
from celery.utils.log import  get_task_logger


app = Celery(main="one", broker="amqp://guest:guest@localhost:5672", backend="rpc://")
logger = get_task_logger(__name__)

# app.config_from_object("celery_conf")

app.conf.update(
    task_time_limit = 60,
    task_soft_time_limit = 50,
    worker_concurrency = 70,
    worker_prefetch_multiplier = 0,
    task_ignore_result = True
)

@app.task(name="adding")
def add(a, b):
    time.sleep(3)
    return a + b



@app.task(bind=True, defualt_retry_delay=600)
def devision(self, a, b):
    try:
        result = a/b
        return result
        
    except ZeroDivisionError:
        logger.info("sorry...")
        self.retry(countdown=10, max_retries=10)



result = add.apply_async((8, 2), link=devision.signature( (2,) ) )
result = add.apply_async((8, 2), link=devision.si(2,1))

   

