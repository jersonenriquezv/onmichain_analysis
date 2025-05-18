import os
import json
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
redis_client = redis.Redis.from_url(REDIS_URL)

def cache_transaction(tx_hash, tx_data):
    redis_client.set(tx_hash, json.dumps(tx_data))

def get_cached_transaction(tx_hash):
    data = redis_client.get(tx_hash)
    if data:
        return json.loads(data)
    return None 