import redis


redis_host = "localhost"
redis_port = 6379
redis_password = ""
redis_db = 0



rd = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password,
    db=redis_db
    )

rd.set("Name", "Sina")
rd.set("Last Name", "Nazem")
rd.set("Job", "Data Scientist")

