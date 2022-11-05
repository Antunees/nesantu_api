import redis


class BrokerPool():

    def __init__(self):
        self.DB0 = redis.StrictRedis(decode_responses=True,
                host="redis-mother", password='q789we677qy87dy7q8wyd9qwd8q79we6391', port=6391, db=0)

        self.DB1 = redis.StrictRedis(decode_responses=True,
                host="redis-mother", password='q789we677qy87dy7q8wyd9qwd8q79we6391', port=6391, db=1)

        self.DB2 = redis.StrictRedis(decode_responses=True,
                host="redis-mother", password='q789we677qy87dy7q8wyd9qwd8q79we6391', port=6391, db=2)

Broker = BrokerPool()
